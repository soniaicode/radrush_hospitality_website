#!/usr/bin/env python3
"""
Email Configuration Test Script
Tests if email sending works with current configuration
"""

import os
from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail, Message

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

print("=" * 60)
print("EMAIL CONFIGURATION TEST")
print("=" * 60)
print(f"MAIL_SERVER: {app.config['MAIL_SERVER']}")
print(f"MAIL_PORT: {app.config['MAIL_PORT']}")
print(f"MAIL_USE_TLS: {app.config['MAIL_USE_TLS']}")
print(f"MAIL_USERNAME: {app.config['MAIL_USERNAME']}")
print(f"MAIL_PASSWORD: {'*' * len(app.config['MAIL_PASSWORD']) if app.config['MAIL_PASSWORD'] else 'NOT SET'}")
print(f"ADMIN_EMAIL: {os.getenv('ADMIN_EMAIL')}")
print("=" * 60)

mail = Mail(app)

def test_email():
    with app.app_context():
        try:
            print("\n🔄 Sending test email...")
            
            admin_email = os.getenv('ADMIN_EMAIL', 'radrushmarketing@gmail.com')
            
            msg = Message(
                subject='✅ Test Email - Radrush Hospitality',
                recipients=[admin_email],
                body='This is a test email to verify email configuration is working correctly.',
                html='<h2>✅ Email Configuration Test</h2><p>This is a test email to verify email configuration is working correctly.</p>'
            )
            
            mail.send(msg)
            print(f"✅ SUCCESS! Test email sent to {admin_email}")
            print("\n✨ Email configuration is working correctly!")
            return True
            
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
            print("\n🔍 Troubleshooting:")
            print("1. Check if MAIL_USERNAME and MAIL_PASSWORD are correct in .env")
            print("2. Verify Gmail App Password is valid (not regular password)")
            print("3. Check if 2-Step Verification is enabled in Gmail")
            print("4. Ensure 'Less secure app access' is enabled (if using regular password)")
            import traceback
            print(f"\n📋 Full error:\n{traceback.format_exc()}")
            return False

if __name__ == '__main__':
    test_email()
