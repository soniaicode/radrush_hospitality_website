#!/usr/bin/env python3
"""
Test script to verify email templates are working correctly
"""
from flask import Flask
from flask_mail import Mail, Message
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

def test_email_templates():
    """Test both email templates"""
    with app.app_context():
        try:
            # Test data
            test_data = {
                'name': 'Test User',
                'email': os.getenv('MAIL_USERNAME'),  # Send to yourself
                'phone': '9876543210',
                'service': 'Hotel Management',
                'message': 'This is a test message to verify email templates are working correctly.',
                'submitted_at': datetime.utcnow().strftime('%B %d, %Y at %I:%M %p')
            }
            
            print("=" * 60)
            print("Testing Email Templates")
            print("=" * 60)
            print(f"From: {app.config['MAIL_USERNAME']}")
            print(f"To: {test_data['email']}")
            print()
            
            # Test Admin Notification Email
            print("1. Testing Admin Notification Email...")
            from flask import render_template
            
            admin_msg = Message(
                subject='🔔 TEST: New Contact - Radrush Hospitality',
                recipients=[test_data['email']],
                html=render_template('emails/admin_notification.html', **test_data)
            )
            
            mail.send(admin_msg)
            print("✅ Admin notification email sent successfully!")
            print()
            
            # Test User Confirmation Email
            print("2. Testing User Confirmation Email...")
            
            user_msg = Message(
                subject='TEST: Thank you for contacting Radrush Hospitality',
                recipients=[test_data['email']],
                html=render_template('emails/user_confirmation.html', **test_data)
            )
            
            mail.send(user_msg)
            print("✅ User confirmation email sent successfully!")
            print()
            
            print("=" * 60)
            print("✅ All email templates tested successfully!")
            print("=" * 60)
            print(f"Check your inbox: {test_data['email']}")
            
        except Exception as e:
            print(f"❌ Error testing emails: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    test_email_templates()
