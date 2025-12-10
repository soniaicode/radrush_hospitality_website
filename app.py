from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

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
            
            # Save to database
            mongo.db.contacts.insert_one(contact_data)
            
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
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
        <h2 style="color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px;">
            New Contact Form Submission
        </h2>
        
        <div style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <p><strong style="color: #667eea;">Name:</strong> {name}</p>
            <p><strong style="color: #667eea;">Email:</strong> <a href="mailto:{email}">{email}</a></p>
            <p><strong style="color: #667eea;">Phone:</strong> {phone or 'Not provided'}</p>
            <p><strong style="color: #667eea;">Service Interested:</strong> {service or 'Not specified'}</p>
        </div>
        
        <div style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <p><strong style="color: #667eea;">Message:</strong></p>
            <p style="background: #f5f5f5; padding: 15px; border-left: 4px solid #667eea; border-radius: 4px;">
                {message}
            </p>
        </div>
        
        <p style="color: #888; font-size: 12px; text-align: center; margin-top: 20px;">
            Submitted at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC
        </p>
    </div>
</body>
</html>
                    """
                )
                mail.send(msg)
                
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
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
        <h2 style="color: #667eea;">Thank you for contacting us!</h2>
        
        <p>Dear <strong>{name}</strong>,</p>
        
        <p>Thank you for reaching out to <strong>Radrush Hospitality</strong>!</p>
        
        <p>We have received your message and will get back to you as soon as possible.</p>
        
        <div style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <h3 style="color: #667eea; margin-top: 0;">Your submitted details:</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone:</strong> {phone or 'Not provided'}</p>
            <p><strong>Service:</strong> {service or 'Not specified'}</p>
        </div>
        
        <div style="background: #667eea; color: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <p style="margin: 0;"><strong>Best regards,</strong></p>
            <p style="margin: 5px 0 0 0;">Radrush Hospitality Team</p>
            <p style="margin: 10px 0 0 0; font-size: 14px;">
                📞 Phone: 7056456555 / 9271900007<br>
                📧 Email: radrushmarketing@gmail.com
            </p>
        </div>
    </div>
</body>
</html>
                    """
                )
                mail.send(user_msg)
                
            except Exception as email_error:
                print(f"Email sending error: {email_error}")
                # Continue even if email fails
            
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash('An error occurred. Please try again.', 'error')
            print(f"Error: {e}")
    
    return render_template('contact.html')

# API Routes for Admin/Dashboard (Optional)
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    try:
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

# Error Handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
