#!/usr/bin/env python3
"""
Test script to verify MongoDB and Email configuration
"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText

load_dotenv()

print("=" * 60)
print("TESTING RADRUSH CONFIGURATION")
print("=" * 60)

# Test 1: Check Environment Variables
print("\n1. CHECKING ENVIRONMENT VARIABLES...")
print("-" * 60)

env_vars = {
    'MONGO_URI': os.getenv('MONGO_URI'),
    'MAIL_SERVER': os.getenv('MAIL_SERVER'),
    'MAIL_PORT': os.getenv('MAIL_PORT'),
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'ADMIN_EMAIL': os.getenv('ADMIN_EMAIL'),
}

for key, value in env_vars.items():
    if value:
        if 'PASSWORD' in key:
            print(f"✅ {key}: {'*' * len(value)}")
        else:
            print(f"✅ {key}: {value}")
    else:
        print(f"❌ {key}: NOT SET")

# Test 2: MongoDB Connection
print("\n2. TESTING MONGODB CONNECTION...")
print("-" * 60)

try:
    mongo_uri = os.getenv('MONGO_URI')
    if mongo_uri:
        # Remove quotes if present
        mongo_uri = mongo_uri.strip('"').strip("'")
        
        print(f"Connecting to: {mongo_uri[:50]}...")
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        
        # Test connection
        client.admin.command('ping')
        print("✅ MongoDB connection successful!")
        
        # List databases
        dbs = client.list_database_names()
        print(f"✅ Available databases: {dbs}")
        
        # Test insert
        db = client.radrush_hospitality
        test_doc = {'test': 'data', 'timestamp': 'test'}
        result = db.test_collection.insert_one(test_doc)
        print(f"✅ Test insert successful! ID: {result.inserted_id}")
        
        # Clean up test
        db.test_collection.delete_one({'_id': result.inserted_id})
        print("✅ Test cleanup successful!")
        
        client.close()
    else:
        print("❌ MONGO_URI not set in .env file")
        
except Exception as e:
    print(f"❌ MongoDB Error: {e}")
    print(f"   Error type: {type(e).__name__}")

# Test 3: Email Configuration
print("\n3. TESTING EMAIL CONFIGURATION...")
print("-" * 60)

try:
    mail_server = os.getenv('MAIL_SERVER')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_username = os.getenv('MAIL_USERNAME')
    mail_password = os.getenv('MAIL_PASSWORD')
    
    if all([mail_server, mail_username, mail_password]):
        print(f"Connecting to {mail_server}:{mail_port}...")
        
        # Create SMTP connection
        server = smtplib.SMTP(mail_server, mail_port)
        server.starttls()
        
        print("✅ SMTP connection established")
        
        # Try login
        server.login(mail_username, mail_password)
        print("✅ Email login successful!")
        
        # Send test email
        admin_email = os.getenv('ADMIN_EMAIL', mail_username)
        msg = MIMEText('This is a test email from Radrush Hospitality configuration test.')
        msg['Subject'] = 'Radrush Test Email'
        msg['From'] = mail_username
        msg['To'] = admin_email
        
        server.send_message(msg)
        print(f"✅ Test email sent to {admin_email}")
        
        server.quit()
        print("✅ Email configuration working perfectly!")
        
    else:
        print("❌ Email configuration incomplete")
        if not mail_server:
            print("   - MAIL_SERVER not set")
        if not mail_username:
            print("   - MAIL_USERNAME not set")
        if not mail_password:
            print("   - MAIL_PASSWORD not set")
            
except Exception as e:
    print(f"❌ Email Error: {e}")
    print(f"   Error type: {type(e).__name__}")

print("\n" + "=" * 60)
print("CONFIGURATION TEST COMPLETE")
print("=" * 60)
