# MongoDB Setup for Render Deployment

## Issue
The error `'NoneType' object has no attribute 'contacts'` occurs because MongoDB is not connected on Render.

## Solution

### Option 1: Use MongoDB Atlas (Recommended - FREE)

1. **Create MongoDB Atlas Account**
   - Go to https://www.mongodb.com/cloud/atlas
   - Sign up for a FREE account
   - Create a new cluster (FREE tier available)

2. **Get Connection String**
   - Click "Connect" on your cluster
   - Choose "Connect your application"
   - Copy the connection string (looks like):
     ```
     mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/radrush_hospitality?retryWrites=true&w=majority
     ```

3. **Add to Render Environment Variables**
   - Go to your Render dashboard
   - Select your web service
   - Go to "Environment" tab
   - Add these variables:
     ```
     MONGO_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/radrush_hospitality?retryWrites=true&w=majority
     SECRET_KEY=your-super-secret-key-change-this
     MAIL_USERNAME=radrushmarketing@gmail.com
     MAIL_PASSWORD=your-gmail-app-password
     ADMIN_EMAIL=radrushmarketing@gmail.com
     ADMIN_USERNAME=radrush_admin
     ADMIN_PASSWORD=Radrush@2024
     ```

4. **Whitelist Render IP**
   - In MongoDB Atlas, go to "Network Access"
   - Click "Add IP Address"
   - Click "Allow Access from Anywhere" (0.0.0.0/0)
   - Or add Render's specific IPs

### Option 2: Work Without Database (Temporary)

The app now handles MongoDB connection failures gracefully:
- Contact form will still send emails
- Data won't be saved to database
- Admin dashboard will show empty data

## Testing

After setting up MongoDB Atlas:
1. Save environment variables in Render
2. Redeploy your service
3. Test the contact form
4. Check admin dashboard for saved contacts

## Important Notes

- **Never commit .env file** with real credentials to GitHub
- Use Render's environment variables for production
- MongoDB Atlas FREE tier includes 512MB storage
- Contact form emails will work even if database fails
