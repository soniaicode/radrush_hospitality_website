# Email Service Fix for Render Deployment

## Problem
Render free tier blocks outbound SMTP connections (ports 587/465) for security reasons, causing email sending to fail with error: `[Errno 101] Network is unreachable`

## Solutions

### Option 1: Use SendGrid (Recommended for Render)
SendGrid provides a free tier with 100 emails/day and works on Render.

#### Steps:
1. **Sign up for SendGrid**: https://signup.sendgrid.com/
2. **Create API Key**:
   - Go to Settings → API Keys
   - Create API Key with "Mail Send" permission
   - Copy the API key

3. **Update Environment Variables on Render**:
   ```
   MAIL_SERVER=smtp.sendgrid.net
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=apikey
   MAIL_PASSWORD=<your-sendgrid-api-key>
   ADMIN_EMAIL=radrushmarketing@gmail.com
   ```

4. **Verify Sender Email**:
   - Go to SendGrid → Settings → Sender Authentication
   - Verify your sender email (radrushmarketing@gmail.com)

### Option 2: Use Mailgun
Mailgun also works on Render with 5,000 free emails/month.

#### Steps:
1. **Sign up**: https://www.mailgun.com/
2. **Get SMTP Credentials** from Mailgun dashboard
3. **Update Environment Variables**:
   ```
   MAIL_SERVER=smtp.mailgun.org
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=<mailgun-smtp-username>
   MAIL_PASSWORD=<mailgun-smtp-password>
   ADMIN_EMAIL=radrushmarketing@gmail.com
   ```

### Option 3: Use Render's Paid Plan
Upgrade to Render's paid plan ($7/month) which allows outbound SMTP connections.

### Option 4: Disable Email Notifications (Temporary)
The app now works without email service. Contact submissions are still saved to MongoDB.

To disable email warnings, remove these environment variables from Render:
- MAIL_USERNAME
- MAIL_PASSWORD

## Current Status
✅ App works without email service
✅ Contact submissions saved to database
⚠️ Email notifications disabled on Render free tier

## Testing Locally
Email works fine locally with Gmail SMTP. The issue is specific to Render's free tier network restrictions.

## Recommended Action
**Use SendGrid** - It's free, reliable, and specifically designed to work with platforms like Render that restrict SMTP.
