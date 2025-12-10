# 🚀 START HERE - Radrush Hospitality Website

## ⚡ Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure MongoDB
Edit `.env` file:
```env
MONGO_URI=mongodb://localhost:27017/radrush_hospitality
```

### Step 3: Run Application
```bash
python app.py
```

Open browser: **http://localhost:5000**

---

## 📚 Complete Documentation

| File | Description |
|------|-------------|
| **README.md** | Complete technical documentation |
| **SETUP_GUIDE.md** | Quick setup instructions (English) |
| **INSTALLATION_HINDI.md** | Installation guide in Hindi |
| **PROJECT_SUMMARY.md** | Project overview and architecture |

---

## 🎯 What You Have

### ✅ Complete Full-Stack Application
- **Frontend:** Modern responsive design with Jinja2 templates
- **Backend:** Flask application with RESTful API
- **Database:** MongoDB integration for contact forms
- **Pages:** Home, About, Services (6 types), Contact

### ✅ Features
- Responsive design (mobile, tablet, desktop)
- Contact form with database storage
- Service-specific pages
- Modern animations and transitions
- Flash message notifications
- Mobile hamburger menu

---

## 📁 Project Structure

```
radrush_hospitality_website/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Configuration (UPDATE THIS!)
├── templates/                # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── services/
└── static/                   # CSS, JS, Images
    ├── css/style.css
    ├── js/script.js
    └── images/logo.png       # ADD YOUR LOGO HERE
```

---

## 🔧 Before Running

### 1. Install Python Packages
```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- Flask-PyMongo (MongoDB integration)
- pymongo (database driver)
- python-dotenv (environment variables)

### 2. Setup MongoDB

**Option A: Local MongoDB**
- Download: https://www.mongodb.com/try/download/community
- Install and run: `mongod`

**Option B: MongoDB Atlas (Free Cloud)**
- Create account: https://www.mongodb.com/cloud/atlas
- Create free cluster
- Get connection string
- Update `.env` file

### 3. Configure Environment
Edit `.env` file:
```env
SECRET_KEY=change-this-to-random-string
MONGO_URI=mongodb://localhost:27017/radrush_hospitality
```

---

## ✅ Verify Setup

Run verification script:
```bash
python verify_setup.py
```

This checks:
- All files present
- Dependencies installed
- Templates exist
- Static files ready

---

## 🎨 Customization

### Update Logo
Replace: `static/images/logo.png`

### Update Contact Info
Edit: `templates/contact.html`
- Phone number
- Email address
- Physical address

### Change Colors
Edit: `static/css/style.css`
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
}
```

---

## 🧪 Testing

### Test Contact Form
1. Go to: http://localhost:5000/contact
2. Fill and submit form
3. Check MongoDB:
```bash
mongo
use radrush_hospitality
db.contacts.find().pretty()
```

### Test All Pages
- Home: http://localhost:5000/
- About: http://localhost:5000/about
- Services: http://localhost:5000/services
- Contact: http://localhost:5000/contact

---

## 🚀 Deployment

### Heroku
```bash
heroku create radrush-hospitality
git push heroku main
```

### Render
1. Connect GitHub repo
2. Build: `pip install -r requirements.txt`
3. Start: `python app.py`

---

## 🆘 Common Issues

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "MongoDB connection failed"
- Check MongoDB is running
- Verify `.env` MONGO_URI
- For Atlas: Check IP whitelist

### "Port 5000 in use"
Change port in `app.py`:
```python
app.run(debug=True, port=8000)
```

---

## 📞 Need Help?

1. Read **README.md** for detailed docs
2. Check **SETUP_GUIDE.md** for quick setup
3. See **INSTALLATION_HINDI.md** for Hindi guide
4. Run `python verify_setup.py` to check setup

---

## 🎉 You're Ready!

If everything is set up:
```bash
python app.py
```

Then open: **http://localhost:5000**

**Next Steps:**
1. ✅ Add your logo
2. ✅ Update contact information
3. ✅ Customize colors and content
4. ✅ Test all features
5. ✅ Deploy to production

---

**Happy Coding! 🚀**

© 2024 Radrush Hospitality. All rights reserved.
