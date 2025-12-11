# Render Email Configuration Setup

## Problem
Emails are not being sent from the deployed Render application.

## Root Cause
Environment variables for email configuration are not set on Render.

## Solution: Add Environment Variables to Render

### Step 1: Go to Render Dashboard
1. Open https://dashboard.render.com
2. Select your service: **radrushhospitality**

### Step 2: Add Environment Variables
Go to **Environment** tab and add these variables:

```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=yogesh.chauhan.ai@gmail.com
MAIL_PASSWORD=oqxrooqczoqwigpb
ADMIN_EMAIL=yogesh.chauhan.ai@gmail.com
```

### Step 3: Save and Redeploy
1. Click **Save Changes**
2. Render will automatically redeploy
3. Wait 2-3 minutes for deployment to complete

## Verify Email is Working

After deployment, test the contact form:
1. Go to https://radrushhospitality.onrender.com/contact
2. Fill and submit the form
3. Check email inbox for confirmation

## Check Logs
View logs at: https://dashboard.render.com/web/[your-service-id]/logs

Look for:
- ✅ `Emails queued for sending` - Good!
- ✅ `Email sent successfully` - Perfect!
- ❌ `Async email error` - Check error message

## Important Notes

### Gmail App Password
- The password `oqxrooqczoqwigpb` is a Gmail App Password
- NOT your regular Gmail password
- Generated from: Google Account → Security → 2-Step Verification → App Passwords

### If Emails Still Don't Work

1. **Check Render Logs** for error messages
2. **Verify Gmail Settings**:
   - 2-Step Verification is enabled
   - App Password is valid
3. **Test locally** first: `python test_email.py`
4. **Check spam folder** - emails might be filtered

## Current Status
- ✅ Email works locally (tested successfully)
- ⏳ Waiting for Render environment variables to be configured
- 🔄 Async email sending implemented (no timeout issues)
