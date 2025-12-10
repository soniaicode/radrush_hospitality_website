# Render Deployment Guide - Radrush Hospitality

## Quick Deployment Steps

### 1. Create Render Account
- Go to https://render.com
- Sign up with GitHub account

### 2. Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `soniaicode/radrush_hospitality_website`
3. Configure the service:

**Basic Settings:**
- Name: `radrush-hospitality`
- Region: Choose closest to your users
- Branch: `main`
- Root Directory: (leave empty)
- Runtime: `Python 3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

**Instance Type:**
- Free (for testing)
- Starter ($7/month for production)

### 3. Add Environment Variables

Click "Environment" tab and add these variables:

```
SECRET_KEY=your-super-secret-key-change-this
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/radrush_hospitality
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=radrushmarketing@gmail.com
MAIL_PASSWORD=your-gmail-app-password
ADMIN_EMAIL=radrushmarketing@gmail.com
```

### 4. MongoDB Setup (MongoDB Atlas)

**Create Free MongoDB Database:**
1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up and create free cluster
3. Create database user (username/password)
4. Whitelist IP: `0.0.0.0/0` (allow all)
5. Get connection string
6. Replace in MONGO_URI above

**Connection String Format:**
```
mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/radrush_hospitality?retryWrites=true&w=majority
```

### 5. Gmail App Password Setup

1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Go to App Passwords
4. Generate password for "Mail"
5. Copy 16-digit password
6. Use in MAIL_PASSWORD environment variable

### 6. Deploy

1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Your site will be live at: `https://radrush-hospitality.onrender.com`

## Important Notes

⚠️ **Free Tier Limitations:**
- Service spins down after 15 minutes of inactivity
- First request after inactivity takes 30-60 seconds
- 750 hours/month free

✅ **Production Ready:**
- Use Starter plan ($7/month) for always-on service
- Add custom domain in Render dashboard
- Enable auto-deploy from GitHub

## Troubleshooting

**Build Failed:**
- Check requirements.txt has all dependencies
- Verify Python version in runtime.txt

**App Crashes:**
- Check environment variables are set correctly
- View logs in Render dashboard

**Database Connection Error:**
- Verify MongoDB Atlas IP whitelist includes 0.0.0.0/0
- Check MONGO_URI format is correct

**Email Not Sending:**
- Verify Gmail App Password is correct
- Check 2-Step Verification is enabled

## Custom Domain Setup

1. Buy domain (GoDaddy, Namecheap, etc.)
2. In Render dashboard → Settings → Custom Domain
3. Add your domain
4. Update DNS records as shown by Render
5. Wait for SSL certificate (automatic)

## Auto-Deploy from GitHub

✅ Already configured! 
- Push to `main` branch
- Render automatically deploys
- Check deployment status in dashboard

## Support

- Render Docs: https://render.com/docs
- MongoDB Atlas Docs: https://docs.atlas.mongodb.com

---

**Your GitHub Repo:** https://github.com/soniaicode/radrush_hospitality_website
**Render Dashboard:** https://dashboard.render.com
