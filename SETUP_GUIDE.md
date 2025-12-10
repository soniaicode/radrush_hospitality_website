# Quick Setup Guide - Radrush Hospitality Website

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Setup MongoDB

**Option A: Local MongoDB**
```bash
# Install MongoDB from: https://www.mongodb.com/try/download/community
# Start MongoDB service
mongod
```

**Option B: MongoDB Atlas (Free Cloud)**
1. Visit: https://www.mongodb.com/cloud/atlas
2. Create free account
3. Create cluster
4. Get connection string
5. Update `.env` file with connection string

### Step 3: Configure Environment
Open `.env` file and update:
```env
SECRET_KEY=your-random-secret-key-here
MONGO_URI=mongodb://localhost:27017/radrush_hospitality
```

### Step 4: Run Application
```bash
python app.py
```

### Step 5: Open Browser
```
http://localhost:5000
```

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] All packages installed (`pip install -r requirements.txt`)
- [ ] MongoDB running (local or Atlas)
- [ ] `.env` file configured
- [ ] Application starts without errors
- [ ] Website opens in browser
- [ ] Contact form works

## 🔧 Common Issues

### Issue: ModuleNotFoundError
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### Issue: MongoDB Connection Error
**Solution**: Check if MongoDB is running
```bash
# Check MongoDB status
mongod --version

# Start MongoDB
mongod
```

### Issue: Port 5000 already in use
**Solution**: Change port in `app.py`
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

## 📝 Testing Contact Form

1. Go to: http://localhost:5000/contact
2. Fill form and submit
3. Check MongoDB for saved data:
```bash
# Open MongoDB shell
mongo

# Use database
use radrush_hospitality

# View contacts
db.contacts.find().pretty()
```

## 🎨 Customization

### Update Logo
Replace: `static/images/logo.png`

### Update Colors
Edit: `static/css/style.css`
```css
:root {
    --primary-color: #2563eb;  /* Change this */
}
```

### Update Contact Info
Edit: `templates/contact.html`

## 📱 Test on Mobile

1. Find your local IP:
```bash
# Windows
ipconfig

# Mac/Linux
ifconfig
```

2. Open on mobile:
```
http://YOUR_IP:5000
```

## 🚀 Production Deployment

### Heroku
```bash
heroku create radrush-hospitality
git push heroku main
```

### Render
1. Connect GitHub repo
2. Build: `pip install -r requirements.txt`
3. Start: `python app.py`

## 📞 Need Help?

- Check README.md for detailed documentation
- Review app.py for route configurations
- Check MongoDB connection in .env file

## 🎉 Success!

If you see the website at http://localhost:5000, you're all set!

Next steps:
1. Add your logo to `static/images/logo.png`
2. Update contact information
3. Test all pages and forms
4. Deploy to production
