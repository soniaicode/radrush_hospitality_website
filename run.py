#!/usr/bin/env python
"""
Quick start script for Radrush Hospitality Website
"""
import os
import sys

def check_requirements():
    """Check if all requirements are installed"""
    try:
        import flask
        import flask_pymongo
        import dotenv
        print("✓ All dependencies installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nPlease run: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists"""
    if os.path.exists('.env'):
        print("✓ .env file found")
        return True
    else:
        print("✗ .env file not found")
        print("\nPlease create .env file with MongoDB configuration")
        return False

def main():
    print("=" * 50)
    print("Radrush Hospitality Website - Startup Check")
    print("=" * 50)
    
    if not check_requirements():
        sys.exit(1)
    
    if not check_env_file():
        sys.exit(1)
    
    print("\n✓ All checks passed!")
    print("\nStarting Flask application...")
    print("=" * 50)
    
    # Import and run the app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
