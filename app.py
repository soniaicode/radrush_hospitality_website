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
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

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
            
            # Send email to admin (with timeout protection)
            try:
                from threading import Thread
                import socket
                
                def send_async_email(flask_app, msg, recipient_type):
                    with flask_app.app_context():
                        try:
                            # Set socket timeout for SMTP
                            socket.setdefaulttimeout(15)
                            print(f"[DEBUG] Sending {recipient_type} email to {msg.recipients}...")
                            mail.send(msg)
                            print(f"[SUCCESS] {recipient_type} email sent to {msg.recipients}")
                            app_logger.info(f"✅ Email sent successfully to {recipient_type}: {msg.recipients}")
                        except Exception as e:
                            print(f"[ERROR] {recipient_type} email failed: {str(e)}")
                            app_logger.error(f"❌ Async email error ({recipient_type}): {str(e)}")
                            import traceback
                            app_logger.error(f"Traceback: {traceback.format_exc()}")
                
                admin_email = os.getenv('ADMIN_EMAIL', 'radrushmarketing@gmail.com')
                submitted_at = datetime.utcnow().strftime('%B %d, %Y at %I:%M %p')
                
                # Email to admin - Using template
                msg = Message(
                    subject=f'🔔 New Contact: {name} - Radrush Hospitality',
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
                    html=render_template('emails/admin_notification.html',
                                       name=name,
                                       email=email,
                                       phone=phone,
                                       service=service,
                                       message=message,
                                       submitted_at=submitted_at)
                )
                
                # Confirmation email to user - Using template
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
                    html=render_template('emails/user_confirmation.html',
                                       name=name,
                                       email=email,
                                       phone=phone,
                                       service=service,
                                       submitted_at=submitted_at)
                )
                
                # Send emails in background threads to avoid blocking
                Thread(target=send_async_email, args=(app, msg, 'admin')).start()
                Thread(target=send_async_email, args=(app, user_msg, 'user')).start()
                
                app_logger.info(f"Emails queued for sending - Admin: {admin_email}, User: {email}")
                
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

# Debug route to check email config (remove in production)
@app.route('/api/email-config-check')
def email_config_check():
    config_status = {
        'MAIL_SERVER': 'SET' if os.getenv('MAIL_SERVER') else 'MISSING',
        'MAIL_PORT': 'SET' if os.getenv('MAIL_PORT') else 'MISSING',
        'MAIL_USERNAME': 'SET' if os.getenv('MAIL_USERNAME') else 'MISSING',
        'MAIL_PASSWORD': 'SET' if os.getenv('MAIL_PASSWORD') else 'MISSING',
        'ADMIN_EMAIL': 'SET' if os.getenv('ADMIN_EMAIL') else 'MISSING',
        'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS', 'NOT SET')
    }
    return jsonify(config_status)

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