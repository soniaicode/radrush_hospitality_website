# Fix Authentication Issues - Radrush Hospitality

## Test Results:
```
❌ MongoDB Error: bad auth : authentication failed
❌ Email Error: Username and Password not accepted
```

## Issue 1: MongoDB Authentication Failed

### Problem:
MongoDB Atlas credentials are incorrect.

### Solution:

1. **Go to MongoDB Atlas:**
   - https://cloud.mongodb.com/

2. **Check Database User:**
   - Click on "Database Access" in left sidebar
   - Check if user "radrush" exists
   - If not, create new user:
     - Username: `radrush`
     - Password: Choose a strong password
     - Database User Privileges: "Read and write to any database"

3. **Get Correct Connection String:**
   - Click on "Database" in left sidebar
   - Click "Connect" button on your cluster
   - Choose "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your actual password
   - Replace `<dbname>` with `radrush_hospitality`

4. **Update .env file:**
   ```env
   MONGO_URI=mongodb+srv://radrush:YOUR_ACTUAL_PASSWORD@cluster0.7dpbzqe.mongodb.net/radrush_hospitality?retryWrites=true&w=majority
   ```

5. **Whitelist IP Address:**
   - Go to "Network Access" in MongoDB Atlas
   - Click "Add IP Address"
   - Choose "Allow Access from Anywhere" (0.0.0.0/0)
   - Or add your specific IP

## Issue 2: Gmail Authentication Failed

### Problem:
Gmail App Password is incorrect or 2-Step Verification is not enabled.

### Solution:

#### Step 1: Enable 2-Step Verification
1. Go to: https://myaccount.google.com/security
2. Under "Signing in to Google", click "2-Step Verification"
3. Follow steps to enable it (if not already enabled)

#### Step 2: Generate New App Password
1. Go to: https://myaccount.google.com/apppasswords
2. If you don't see this option, make sure 2-Step Verification is ON
3. Select app: "Mail"
4. Select device: "Other (Custom name)"
5. Enter name: "Radrush Website"
6. Click "Generate"
7. **Copy the 16-character password** (example: `abcd efgh ijkl mnop`)
8. **Remove all spaces**: `abcdefghijklmnop`

#### Step 3: Update .env file
```env
MAIL_USERNAME=yogesh.chauhan.ai@gmail.com
MAIL_PASSWORD=abcdefghijklmnop
```

**IMPORTANT:** 
- Use the 16-character App Password, NOT your regular Gmail password
- Remove all spaces from the App Password
- Don't use quotes around the password

## Complete .env File Example:

```env
# Flask Configuration
SECRET_KEY=radrush-secret-key-2024-production
FLASK_ENV=development
FLASK_DEBUG=True

# MongoDB Configuration (UPDATE THIS)
MONGO_URI=mongodb+srv://radrush:YOUR_MONGODB_PASSWORD@cluster0.7dpbzqe.mongodb.net/radrush_hospitality?retryWrites=true&w=majority

# Email Configuration (UPDATE THIS)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=yogesh.chauhan.ai@gmail.com
MAIL_PASSWORD=your16charapppassword
ADMIN_EMAIL=yogesh.chauhan.ai@gmail.com

# Admin Dashboard Credentials
ADMIN_USERNAME=radrush_admin
ADMIN_PASSWORD=Radrush@2024
```

## Testing After Fix:

1. **Update .env file** with correct credentials
2. **Run test script:**
   ```bash
   python test_config.py
   ```
3. **Look for:**
   ```
   ✅ MongoDB connection successful!
   ✅ Email login successful!
   ✅ Test email sent
   ```

## For Render Deployment:

After fixing locally, update Render environment variables:

1. Go to Render Dashboard
2. Select your web service
3. Go to "Environment" tab
4. Update these variables with correct values:
   - `MONGO_URI`
   - `MAIL_PASSWORD`
5. Save changes
6. Render will automatically redeploy

## Quick Checklist:

- [ ] MongoDB user exists in Atlas
- [ ] MongoDB password is correct
- [ ] IP address is whitelisted in MongoDB Atlas
- [ ] Gmail 2-Step Verification is enabled
- [ ] Gmail App Password is generated
- [ ] App Password has no spaces
- [ ] .env file is updated
- [ ] Test script passes
- [ ] Render environment variables updated

## Need Help?

Run the test script to see detailed error messages:
```bash
python test_config.py
```
