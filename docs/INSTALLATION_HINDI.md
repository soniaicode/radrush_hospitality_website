# Radrush Hospitality Website - Installation Guide (Hindi)

## 🚀 Complete Setup Guide

### Step 1: Python Install Karo

1. Python download karo: https://www.python.org/downloads/
2. Version 3.8 ya usse upar install karo
3. Installation ke time "Add Python to PATH" check karo

Verify karo:
```bash
python --version
```

### Step 2: Project Setup

1. Project folder mein jao:
```bash
cd radrush_hospitality_website
```

2. Virtual environment banao (optional but recommended):
```bash
python -m venv venv
```

3. Virtual environment activate karo:
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Dependencies Install Karo

```bash
pip install -r requirements.txt
```

Ye packages install honge:
- Flask (web framework)
- Flask-PyMongo (MongoDB integration)
- pymongo (MongoDB driver)
- python-dotenv (environment variables)

### Step 4: MongoDB Setup

**Option A: Local MongoDB (Recommended for Development)**

1. MongoDB download karo: https://www.mongodb.com/try/download/community
2. Install karo (default settings theek hai)
3. MongoDB start karo:
   ```bash
   mongod
   ```

**Option B: MongoDB Atlas (Free Cloud Database)**

1. Account banao: https://www.mongodb.com/cloud/atlas
2. Free cluster create karo (M0 Sandbox)
3. Database user banao
4. Network Access mein apna IP add karo (ya 0.0.0.0/0 for all)
5. Connection string copy karo

### Step 5: Environment Variables Configure Karo

`.env` file open karo aur update karo:

**Local MongoDB ke liye:**
```env
SECRET_KEY=apni-secret-key-yaha-likho
MONGO_URI=mongodb://localhost:27017/radrush_hospitality
FLASK_ENV=development
FLASK_DEBUG=True
```

**MongoDB Atlas ke liye:**
```env
SECRET_KEY=apni-secret-key-yaha-likho
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/radrush_hospitality?retryWrites=true&w=majority
FLASK_ENV=development
FLASK_DEBUG=True
```

**Important:** SECRET_KEY ko change karo ek random string se!

### Step 6: Setup Verify Karo

```bash
python verify_setup.py
```

Ye script check karega ki sab kuch theek se setup hai ya nahi.

### Step 7: Application Run Karo

```bash
python app.py
```

Ya:
```bash
python run.py
```

Agar sab theek hai to ye message dikhega:
```
* Running on http://0.0.0.0:5000
```

### Step 8: Browser Mein Open Karo

```
http://localhost:5000
```

## ✅ Testing

### Contact Form Test Karo

1. Contact page par jao: http://localhost:5000/contact
2. Form fill karo
3. Submit karo
4. Success message dikhna chahiye

### MongoDB Mein Data Check Karo

```bash
# MongoDB shell open karo
mongo

# Database select karo
use radrush_hospitality

# Contacts dekho
db.contacts.find().pretty()
```

## 🎨 Customization

### 1. Logo Update Karo

Apna logo `static/images/logo.png` mein replace karo

### 2. Contact Information Update Karo

`templates/contact.html` file open karo aur update karo:
- Phone number
- Email address
- Physical address

### 3. Colors Change Karo

`static/css/style.css` file mein:
```css
:root {
    --primary-color: #2563eb;     /* Apna color yaha */
    --secondary-color: #1e40af;   /* Apna color yaha */
    --accent-color: #3b82f6;      /* Apna color yaha */
}
```

### 4. Content Update Karo

Templates folder mein jao aur HTML files edit karo:
- `templates/index.html` - Home page
- `templates/about.html` - About page
- `templates/services/` - Service pages

## 🔧 Common Problems & Solutions

### Problem 1: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem 2: "MongoDB connection failed"
**Solution:**
- Check karo MongoDB running hai ya nahi
- `.env` file mein MONGO_URI check karo
- MongoDB Atlas use kar rahe ho to IP whitelist check karo

### Problem 3: "Port 5000 already in use"
**Solution:**
`app.py` mein port change karo:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

### Problem 4: "Template not found"
**Solution:**
- Check karo `templates` folder exist karta hai
- Check karo sab template files present hai

## 📱 Mobile Pe Test Karo

1. Apna local IP find karo:
```bash
# Windows
ipconfig

# Mac/Linux
ifconfig
```

2. Mobile browser mein open karo:
```
http://YOUR_IP_ADDRESS:5000
```

**Note:** Mobile aur computer same WiFi network pe hone chahiye!

## 🚀 Production Deployment

### Heroku Pe Deploy Karo

1. Heroku account banao
2. Heroku CLI install karo
3. Commands run karo:
```bash
heroku login
heroku create radrush-hospitality
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

### Render Pe Deploy Karo

1. GitHub pe code push karo
2. Render.com pe account banao
3. New Web Service create karo
4. GitHub repo connect karo
5. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
6. Environment variables add karo (.env file se)

## 📊 Database Structure

### Contacts Collection
```json
{
  "name": "Customer Name",
  "email": "email@example.com",
  "phone": "+91 1234567890",
  "service": "hotels",
  "message": "Message text",
  "created_at": "2024-12-01T10:30:00",
  "status": "new"
}
```

## 🎯 Features

✅ Responsive design (mobile, tablet, desktop)
✅ Contact form with MongoDB storage
✅ Service-specific pages
✅ Modern animations
✅ Flash messages
✅ SEO friendly
✅ Fast loading

## 📞 Help Chahiye?

1. README.md file padho
2. SETUP_GUIDE.md dekho
3. verify_setup.py run karo
4. MongoDB connection check karo

## 🎉 Success!

Agar website http://localhost:5000 pe dikh rahi hai, to congratulations! 🎊

**Next Steps:**
1. Logo add karo
2. Contact info update karo
3. Content customize karo
4. Test karo sab pages
5. Production pe deploy karo

**Happy Coding! 🚀**
