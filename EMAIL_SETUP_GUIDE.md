# Email Setup Guide for Radrush Hospitality

## Issue
Contact form emails are not being sent because Gmail password is not configured properly.

## Solution: Gmail App Password Setup

### Step 1: Enable 2-Step Verification
1. Go to your Google Account: https://myaccount.google.com/
2. Click on "Security" in the left sidebar
3. Under "Signing in to Google", click "2-Step Verification"
4. Follow the steps to enable it (if not already enabled)

### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select app: "Mail"
3. Select device: "Other (Custom name)"
4. Enter name: "Radrush Website"
5. Click "Generate"
6. **Copy the 16-character password** (looks like: `abcd efgh ijkl mnop`)

### Step 3: Update Environment Variables

#### For Local Development (.env file):
```env
MAIL_USERNAME=radrushmarketing@gmail.com
MAIL_PASSWORD=abcdefghijklmnop
ADMIN_EMAIL=radrushmarketing@gmail.com
```

#### For Render Deployment:
1. Go to Render Dashboard
2. Select your web service
3. Go to "Environment" tab
4. Add/Update these variables:
   ```
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=radrushmarketing@gmail.com
   MAIL_PASSWORD=your-16-char-app-password
   ADMIN_EMAIL=radrushmarketing@gmail.com
   ```

### Step 4: Test Email
1. Go to contact page
2. Fill the form
3. Submit
4. Check:
   - Admin email (radrushmarketing@gmail.com) should receive notification
   - User should receive confirmation email
   - Check spam folder if not in inbox

## Important Notes

⚠️ **Never use your regular Gmail password** - Always use App Password
⚠️ **Remove spaces** from the 16-character app password
⚠️ **Don't commit .env file** with real passwords to GitHub
⚠️ **Use Render environment variables** for production

## Troubleshooting

### If emails still not working:

1. **Check Render Logs:**
   ```
   Look for: "Email sending error"
   ```

2. **Verify Gmail Settings:**
   - 2-Step Verification is ON
   - App Password is generated
   - Less secure app access is NOT needed (we use App Password)

3. **Check Email in Code:**
   - Open browser console
   - Look for error messages
   - Check network tab for failed requests

4. **Test Locally First:**
   ```bash
   python app.py
   ```
   - Fill contact form
   - Check terminal for errors

## Alternative: Use SendGrid (Free Tier)

If Gmail doesn't work, you can use SendGrid:

1. Sign up: https://sendgrid.com/
2. Get API key
3. Update .env:
   ```env
   MAIL_SERVER=smtp.sendgrid.net
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=apikey
   MAIL_PASSWORD=your-sendgrid-api-key
   ```

## Contact Form Flow

1. User fills form → Submit
2. Data saved to MongoDB (if connected)
3. Email sent to admin (radrushmarketing@gmail.com)
4. Confirmation email sent to user
5. Success message shown

Even if MongoDB is not connected, emails will still be sent!
