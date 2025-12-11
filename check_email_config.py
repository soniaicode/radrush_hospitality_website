"""
Quick diagnostic script to check email configuration on Render
Run this on Render to verify environment variables
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("ENVIRONMENT VARIABLES CHECK")
print("=" * 60)

vars_to_check = [
    'MAIL_SERVER',
    'MAIL_PORT', 
    'MAIL_USE_TLS',
    'MAIL_USERNAME',
    'MAIL_PASSWORD',
    'ADMIN_EMAIL'
]

for var in vars_to_check:
    value = os.getenv(var)
    if var == 'MAIL_PASSWORD':
        display = f"{'*' * len(value) if value else 'NOT SET'}"
    else:
        display = value if value else 'NOT SET'
    
    status = "✅" if value else "❌"
    print(f"{status} {var}: {display}")

print("=" * 60)

# Check if all required vars are set
missing = [v for v in vars_to_check if not os.getenv(v)]
if missing:
    print(f"\n❌ MISSING: {', '.join(missing)}")
    print("\nAdd these to Render Environment Variables!")
else:
    print("\n✅ All email configuration variables are set!")
