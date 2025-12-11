from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from functools import wraps
import hashlib

load_dotenv()

# Setup logging
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/contact_submissions.log', maxBytes=10240000, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)

app_logger = logging.getLogger('radrush_app')
app_logger.setLevel(logging.INFO)
app_logger.addHandler(file_handler)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/radrush_hospitality')

# Email Configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mongo = PyMongo(app)
mail = Mail(app)

# Admin credentials (stored securely)
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'radrush_admin')
ADMIN_PASSWORD_HASH = hashlib.sha256(os.getenv('ADMIN_PASSWORD', 'Radrush@2024').encode()).hexdigest()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Please login to access admin dashboard', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Services Routes
@app.route('/services')
def services():
    return render_template('services/index.html')

@app.route('/services/hotels')
def hotels():
    return render_template('services/hotels.html')

@app.route('/services/resorts')
def resorts():
    return render_template('services/resorts.html')

@app.route('/services/gyms')
def gyms():
    return render_template('services/gyms.html')

@app.route('/services/clubs-pubs')
def clubs_pubs():
    return render_template('services/clubs-pubs.html')

@app.route('/services/wedding-planning')
def wedding_planning():
    return render_template('services/wedding-planning.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            service = request.form.get('service')
            message = request.form.get('message')
            
            contact_data = {
                'name': name,
                'email': email,
                'phone': phone,
                'service': service,
                'message': message,
                'created_at': datetime.utcnow(),
                'status': 'new'
            }
            
            # Save to database (with error handling for MongoDB connection)
            try:
                if mongo.db is not None:
                    result = mongo.db.contacts.insert_one(contact_data)
                    app_logger.info(f"New contact saved to database - ID: {result.inserted_id}, Name: {name}, Email: {email}")
                else:
                    app_logger.warning(f"MongoDB not connected. Contact data not saved: {name} ({email})")
            except Exception as db_error:
                app_logger.error(f"Database error: {db_error}. Contact: {name} ({email})")
                print(f"Database error: {db_error}")
            
            # Send email to admin
            try:
                admin_email = os.getenv('ADMIN_EMAIL', 'radrushmarketing@gmail.com')
                
                # Email to admin
                msg = Message(
                    subject=f'New Contact Form Submission - {name}',
                    recipients=[admin_email],
                    body=f"""
New Contact Form Submission

Name: {name}
Email: {email}
Phone: {phone or 'Not provided'}
Service Interested: {service or 'Not specified'}

Message:
{message}

Submitted at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC
                    """,
                    html=f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 20px;">
        <tr>
            <td align="center">
                <!-- Main Container -->
                <table width="600" cellpadding="0" cellspacing="0" style="background: white; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); overflow: hidden; max-width: 100%;">
                    
                    <!-- Header with Logo and Brand -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                            <div style="background: white; width: 80px; height: 80px; border-radius: 20px; margin: 0 auto 20px; display: inline-flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                                <span style="font-size: 40px; font-weight: 900; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">R</span>
                            </div>
                            <h1 style="margin: 0; color: white; font-size: 32px; font-weight: 800; letter-spacing: -0.5px;">Radrush Hospitality</h1>
                            <p style="margin: 10px 0 0; color: rgba(255,255,255,0.9); font-size: 14px; font-weight: 500; letter-spacing: 2px; text-transform: uppercase;">New Contact Inquiry</p>
                        </td>
                    </tr>
                    
                    <!-- Alert Badge -->
                    <tr>
                        <td style="padding: 30px 30px 0;">
                            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 15px 25px; border-radius: 50px; display: inline-block; font-weight: 700; font-size: 14px; box-shadow: 0 8px 20px rgba(245,87,108,0.3);">
                                🔔 New Lead Alert
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Contact Information Cards -->
                    <tr>
                        <td style="padding: 30px;">
                            
                            <!-- Name Card -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px; margin-bottom: 15px; overflow: hidden;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td width="50" style="vertical-align: top;">
                                                    <div style="width: 45px; height: 45px; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold;">
                                                        👤
                                                    </div>
                                                </td>
                                                <td style="padding-left: 15px;">
                                                    <p style="margin: 0; font-size: 12px; color: #666; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Full Name</p>
                                                    <p style="margin: 5px 0 0; font-size: 18px; color: #1a1a1a; font-weight: 700;">{name}</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Email Card -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); border-radius: 15px; margin-bottom: 15px; overflow: hidden;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td width="50" style="vertical-align: top;">
                                                    <div style="width: 45px; height: 45px; background: linear-gradient(135deg, #f093fb, #f5576c); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold;">
                                                        📧
                                                    </div>
                                                </td>
                                                <td style="padding-left: 15px;">
                                                    <p style="margin: 0; font-size: 12px; color: #666; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Email Address</p>
                                                    <p style="margin: 5px 0 0; font-size: 16px; color: #1a1a1a; font-weight: 600;"><a href="mailto:{email}" style="color: #f5576c; text-decoration: none;">{email}</a></p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Phone Card -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); border-radius: 15px; margin-bottom: 15px; overflow: hidden;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td width="50" style="vertical-align: top;">
                                                    <div style="width: 45px; height: 45px; background: linear-gradient(135deg, #4facfe, #00f2fe); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold;">
                                                        📱
                                                    </div>
                                                </td>
                                                <td style="padding-left: 15px;">
                                                    <p style="margin: 0; font-size: 12px; color: #666; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Phone Number</p>
                                                    <p style="margin: 5px 0 0; font-size: 18px; color: #1a1a1a; font-weight: 700;">{phone or 'Not provided'}</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Service Card -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); border-radius: 15px; margin-bottom: 20px; overflow: hidden;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td width="50" style="vertical-align: top;">
                                                    <div style="width: 45px; height: 45px; background: linear-gradient(135deg, #fa709a, #fee140); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold;">
                                                        🎯
                                                    </div>
                                                </td>
                                                <td style="padding-left: 15px;">
                                                    <p style="margin: 0; font-size: 12px; color: #666; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Service Interested</p>
                                                    <p style="margin: 5px 0 0; font-size: 18px; color: #1a1a1a; font-weight: 700;">{service or 'Not specified'}</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Message Card -->
                            <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(102,126,234,0.3);">
                                <tr>
                                    <td style="padding: 25px;">
                                        <p style="margin: 0 0 15px; font-size: 14px; color: rgba(255,255,255,0.9); font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">💬 Message</p>
                                        <div style="background: rgba(255,255,255,0.95); padding: 20px; border-radius: 12px; border-left: 5px solid #f5576c;">
                                            <p style="margin: 0; color: #333; font-size: 16px; line-height: 1.8; font-weight: 500;">{message}</p>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                            
                        </td>
                    </tr>
                    
                    <!-- Action Button -->
                    <tr>
                        <td style="padding: 0 30px 30px; text-align: center;">
                            <a href="mailto:{email}" style="display: inline-block; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 18px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 16px; box-shadow: 0 10px 30px rgba(245,87,108,0.4); transition: all 0.3s;">
                                📧 Reply to {name.split()[0]}
                            </a>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e0e0e0;">
                            <p style="margin: 0 0 10px; color: #666; font-size: 13px; font-weight: 600;">
                                ⏰ Submitted at: {datetime.utcnow().strftime('%B %d, %Y at %I:%M %p')} UTC
                            </p>
                            <p style="margin: 10px 0 0; color: #999; font-size: 12px;">
                                © 2024 Radrush Hospitality. All rights reserved.
                            </p>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
                    """
                )
                mail.send(msg)
                app_logger.info(f"Admin notification email sent to {admin_email} for contact from {name}")
                
                # Confirmation email to user
                user_msg = Message(
                    subject='Thank you for contacting Radrush Hospitality',
                    recipients=[email],
                    body=f"""
Dear {name},

Thank you for reaching out to Radrush Hospitality!

We have received your message and will get back to you as soon as possible.

Your submitted details:
- Name: {name}
- Email: {email}
- Phone: {phone or 'Not provided'}
- Service: {service or 'Not specified'}

Best regards,
Radrush Hospitality Team
Phone: 7056456555 / 9271900007
Email: radrushmarketing@gmail.com
                    """,
                    html=f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
    <table width="100%" cellpadding="0" cellspacing="0" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 20px;">
        <tr>
            <td align="center">
                <!-- Main Container -->
                <table width="600" cellpadding="0" cellspacing="0" style="background: white; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); overflow: hidden; max-width: 100%;">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 30px; text-align: center;">
                            <div style="background: white; width: 100px; height: 100px; border-radius: 50%; margin: 0 auto 25px; display: inline-flex; align-items: center; justify-content: center; box-shadow: 0 15px 40px rgba(0,0,0,0.2);">
                                <span style="font-size: 50px;">✅</span>
                            </div>
                            <h1 style="margin: 0; color: white; font-size: 36px; font-weight: 800; letter-spacing: -0.5px;">Thank You!</h1>
                            <p style="margin: 15px 0 0; color: rgba(255,255,255,0.95); font-size: 18px; font-weight: 500;">We've received your message</p>
                        </td>
                    </tr>
                    
                    <!-- Welcome Message -->
                    <tr>
                        <td style="padding: 40px 30px 30px;">
                            <h2 style="margin: 0 0 20px; color: #1a1a1a; font-size: 24px; font-weight: 700;">Dear {name},</h2>
                            <p style="margin: 0 0 20px; color: #555; font-size: 16px; line-height: 1.8;">
                                Thank you for reaching out to <strong style="color: #667eea;">Radrush Hospitality</strong>! 
                                We're excited to connect with you and learn more about how we can help elevate your hospitality business.
                            </p>
                            <p style="margin: 0; color: #555; font-size: 16px; line-height: 1.8;">
                                Our team will review your inquiry and get back to you within <strong style="color: #f5576c;">24 hours</strong>.
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Submission Details -->
                    <tr>
                        <td style="padding: 0 30px 30px;">
                            <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px; padding: 25px; border-left: 5px solid #667eea;">
                                <h3 style="margin: 0 0 20px; color: #667eea; font-size: 18px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">📋 Your Submission Details</h3>
                                
                                <table width="100%" cellpadding="8" cellspacing="0">
                                    <tr>
                                        <td style="color: #666; font-size: 14px; font-weight: 600; width: 140px;">Name:</td>
                                        <td style="color: #1a1a1a; font-size: 15px; font-weight: 700;">{name}</td>
                                    </tr>
                                    <tr>
                                        <td style="color: #666; font-size: 14px; font-weight: 600;">Email:</td>
                                        <td style="color: #667eea; font-size: 15px; font-weight: 600;">{email}</td>
                                    </tr>
                                    <tr>
                                        <td style="color: #666; font-size: 14px; font-weight: 600;">Phone:</td>
                                        <td style="color: #1a1a1a; font-size: 15px; font-weight: 700;">{phone or 'Not provided'}</td>
                                    </tr>
                                    <tr>
                                        <td style="color: #666; font-size: 14px; font-weight: 600;">Service:</td>
                                        <td style="color: #1a1a1a; font-size: 15px; font-weight: 700;">{service or 'Not specified'}</td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- What's Next Section -->
                    <tr>
                        <td style="padding: 0 30px 30px;">
                            <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); border-radius: 15px; padding: 25px;">
                                <h3 style="margin: 0 0 15px; color: #d35400; font-size: 18px; font-weight: 700;">🚀 What Happens Next?</h3>
                                <ul style="margin: 0; padding-left: 20px; color: #555; font-size: 15px; line-height: 2;">
                                    <li>Our team reviews your inquiry</li>
                                    <li>We'll contact you within 24 hours</li>
                                    <li>Discuss your specific needs</li>
                                    <li>Create a customized solution for you</li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Contact Information -->
                    <tr>
                        <td style="padding: 0 30px 40px;">
                            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 30px; text-align: center; color: white;">
                                <h3 style="margin: 0 0 20px; font-size: 20px; font-weight: 700;">Need Immediate Assistance?</h3>
                                <p style="margin: 0 0 20px; font-size: 15px; opacity: 0.95;">Feel free to reach out to u
                       
                                <ta">
                                    <tr>
                >
                                            
                                                <p style="margin: 0; font-size: 14pe</p>
                                                <p style="ma</p>
                                            </
            td>
                                    </tr>
                                    <tr>
                                        <td ali">
                              ">
                                                <p style="margin: 0Email</p>
                                                <p style="margin: il.com</p>
                                iv>
    >
                                    </tr>
/table>
                            </div>
                        </td>
                   </tr>
                
                    <!-- Foo
                    <tr>
        >
                            <p style="margin: 0 0 10px; color: #1a1a1a; 
                                s,<br>
                                <span style="col>
                            </p>
                            <p style="margin: 15px 0 0; color: px;">
                          
                            </p>
 </td>
                    </tr>
                
        >
            </td>
        </tr>
    </tae>
</body>
</html>
        """            blable/t        <                           eserved.rights rality. All drush Hospit   © 2024 Ra   : 12ont-size99; f#9 Team</spanlityush Hospita">Radr #667eea;r:oBest regard">ght: 700; font-wei 16px;font-size:;" #e0e0e0 solidr-top: 1pxter; borde-align: cenx; textg: 30pddinpa9fa; und: #f8fbackgrostyle=" <td                ->ter -               <                      /td <                                    </d           ng@gmarketiradrushmaht: 700;">nt-weig: 16px; font-size 0 0; fo5px0.9;">📧 ty: ci; opaze: 14px; font-si 5px;argin:e-block; mlindisplay: in; ing: 15px: 12px; paddr-radius borde5,0.2);25,255,(255baground: rg="back style      <div        centergn="        </                    iv>d0007719055 / 92>70564565 700;"-weight:x; fontnt-size: 16p0; foin: 5px 0 rg📞 Phony: 0.9;">it; opacx 5px;">in:margline-block; : insplaydi; ng: 15pxddi: 12px; paiusad border-r2);,255,255,0.gba(255nd: rbackgrouyle="<div str""centetd align=      <                  pacing="0lls0" cedding="1" cellpadth="100%ble wi         </p>ly:s direct
                )
                mail.send(user_msg)
                app_logger.info(f"Confirmation email sent to user: {email}")
                
            except Exception as email_error:
                app_logger.error(f"Email sending error for {email}: {email_error}")
                print(f"Email sending error: {email_error}")
                # Continue even if email fails
            
            flash('Thank you for your message! We will get back to you soon.', 'success')
            app_logger.info(f"Contact form submission completed successfully for {name} ({email})")
            return redirect(url_for('contact'))
        except Exception as e:
            app_logger.error(f"Error processing contact form: {e}")
            flash('An error occurred. Please try again.', 'error')
            print(f"Error: {e}")
    
    return render_template('contact.html')

# API Routes for Admin/Dashboard (Optional)
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    try:
        if mongo.db is None:
            return jsonify({'success': False, 'error': 'Database not connected'}), 500
        
        contacts = list(mongo.db.contacts.find().sort('created_at', -1))
        for contact in contacts:
            contact['_id'] = str(contact['_id'])
            contact['created_at'] = contact['created_at'].isoformat()
        return jsonify({'success': True, 'contacts': contacts})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    try:
        if mongo.db is None:
            return jsonify({'success': False, 'error': 'Database not connected'}), 500
        
        total_contacts = mongo.db.contacts.count_documents({})
        new_contacts = mongo.db.contacts.count_documents({'status': 'new'})
        
        stats = {
            'total_contacts': total_contacts,
            'new_contacts': new_contacts,
            'total_clients': 500,  # Static for now
            'campaigns': 1000  # Static for now
        }
        return jsonify({'success': True, 'stats': stats})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Admin Login Route
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if 'admin_logged_in' in session:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if username == ADMIN_USERNAME and password_hash == ADMIN_PASSWORD_HASH:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            app_logger.info(f"Admin login successful: {username}")
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            app_logger.warning(f"Failed login attempt for username: {username}")
            flash('Invalid username or password', 'error')
    
    return render_template('admin_login.html')

# Admin Logout Route
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('admin_login'))

# Admin Dashboard Route
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    try:
        if mongo.db is None:
            app_logger.error("MongoDB not connected")
            flash('Database connection error. Please check configuration.', 'error')
            return render_template('admin_dashboard.html', contacts=[], stats={'total': 0, 'today': 0, 'week': 0, 'month': 0})
        
        # Get filter parameters
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        service_filter = request.args.get('service')
        
        # Build query
        query = {}
        
        if from_date:
            from_datetime = datetime.strptime(from_date, '%Y-%m-%d')
            query['created_at'] = {'$gte': from_datetime}
        
        if to_date:
            to_datetime = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1)
            if 'created_at' in query:
                query['created_at']['$lt'] = to_datetime
            else:
                query['created_at'] = {'$lt': to_datetime}
        
        if service_filter:
            query['service'] = service_filter
        
        # Get contacts with filters
        contacts = list(mongo.db.contacts.find(query).sort('created_at', -1))
        
        # Calculate stats
        now = datetime.utcnow()
        today_start = datetime(now.year, now.month, now.day)
        week_start = now - timedelta(days=7)
        month_start = datetime(now.year, now.month, 1)
        
        stats = {
            'total': mongo.db.contacts.count_documents({}),
            'today': mongo.db.contacts.count_documents({'created_at': {'$gte': today_start}}),
            'week': mongo.db.contacts.count_documents({'created_at': {'$gte': week_start}}),
            'month': mongo.db.contacts.count_documents({'created_at': {'$gte': month_start}})
        }
        
        return render_template('admin_dashboard.html', contacts=contacts, stats=stats)
    except Exception as e:
        app_logger.error(f"Error loading admin dashboard: {e}")
        flash('Error loading dashboard', 'error')
        return render_template('admin_dashboard.html', contacts=[], stats={'total': 0, 'today': 0, 'week': 0, 'month': 0})

# Error Handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
