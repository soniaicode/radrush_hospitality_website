#!/usr/bin/env python
"""
Setup Verification Script for Radrush Hospitality Website
"""
import os
import sys

def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def check_file(filepath, description):
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description}: {filepath} NOT FOUND")
        return False

def check_directory(dirpath, description):
    if os.path.isdir(dirpath):
        print(f"✓ {description}: {dirpath}")
        return True
    else:
        print(f"✗ {description}: {dirpath} NOT FOUND")
        return False

def main():
    print_header("Radrush Hospitality - Setup Verification")
    
    all_good = True
    
    # Check main files
    print("\n📄 Checking Main Files:")
    all_good &= check_file("app.py", "Flask Application")
    all_good &= check_file("requirements.txt", "Requirements File")
    all_good &= check_file(".env", "Environment File")
    all_good &= check_file("README.md", "Documentation")
    
    # Check directories
    print("\n📁 Checking Directories:")
    all_good &= check_directory("templates", "Templates Folder")
    all_good &= check_directory("static", "Static Files Folder")
    all_good &= check_directory("static/css", "CSS Folder")
    all_good &= check_directory("static/js", "JavaScript Folder")
    all_good &= check_directory("static/images", "Images Folder")
    
    # Check templates
    print("\n📝 Checking Templates:")
    all_good &= check_file("templates/base.html", "Base Template")
    all_good &= check_file("templates/index.html", "Home Page")
    all_good &= check_file("templates/about.html", "About Page")
    all_good &= check_file("templates/contact.html", "Contact Page")
    all_good &= check_file("templates/services/index.html", "Services Page")
    all_good &= check_file("templates/services/hotels.html", "Hotels Page")
    all_good &= check_file("templates/services/resorts.html", "Resorts Page")
    all_good &= check_file("templates/services/gyms.html", "Gyms Page")
    all_good &= check_file("templates/services/clubs-pubs.html", "Clubs Page")
    all_good &= check_file("templates/services/wedding-planning.html", "Wedding Page")
    
    # Check static files
    print("\n🎨 Checking Static Files:")
    all_good &= check_file("static/css/style.css", "Main CSS")
    all_good &= check_file("static/js/script.js", "Main JavaScript")
    
    # Check Python packages
    print("\n📦 Checking Python Packages:")
    try:
        import flask
        print(f"✓ Flask {flask.__version__} installed")
    except ImportError:
        print("✗ Flask NOT installed")
        all_good = False
    
    try:
        import flask_pymongo
        print("✓ Flask-PyMongo installed")
    except ImportError:
        print("✗ Flask-PyMongo NOT installed")
        all_good = False
    
    try:
        import pymongo
        print(f"✓ PyMongo {pymongo.__version__} installed")
    except ImportError:
        print("✗ PyMongo NOT installed")
        all_good = False
    
    try:
        import dotenv
        print("✓ python-dotenv installed")
    except ImportError:
        print("✗ python-dotenv NOT installed")
        all_good = False
    
    # Final result
    print_header("Verification Result")
    if all_good:
        print("\n✅ ALL CHECKS PASSED!")
        print("\nYou're ready to run the application:")
        print("   python app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print("\n❌ SOME CHECKS FAILED!")
        print("\nPlease fix the issues above before running.")
        print("\nTo install missing packages:")
        print("   pip install -r requirements.txt")
    
    print("\n" + "=" * 60 + "\n")
    
    return 0 if all_good else 1

if __name__ == '__main__':
    sys.exit(main())
