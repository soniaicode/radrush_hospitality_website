# 📧 Contact Form Email - Quick Start

## ✅ Kya Complete Ho Gaya

Contact form ab fully functional hai with email notifications!

### Features:
- ✅ User form submit karta hai → Admin ko email jayega
- ✅ User ko automatic confirmation email jayega
- ✅ Database mein save hoga (MongoDB)
- ✅ Beautiful HTML email templates
- ✅ Success/Error messages on website

---

## 🚀 Setup (2 Steps)

### Step 1: .env File Update Karein

Apna **existing Gmail password** use karein:

```env
MAIL_USERNAME=radrushmarketing@gmail.com
MAIL_PASSWORD=your-actual-password
ADMIN_EMAIL=radrushmarketing@gmail.com
```

**Note:** Agar 2-Step Verification ON hai, to App Password chahiye (details neeche)

### Step 2: Install & Run

```bash
# Install Flask-Mail
pip install Flask-Mail

# Test email configuration
python test_email.py

# Run server
python run.py
```

---

## 🧪 Testing

1. Website kholen: http://localhost:5000/contact
2. Form fill karein
3. Submit karein
4. Check:
   - ✅ Admin email mein notification
   - ✅ User email mein confirmation
   - ✅ Success message on website

---

## 📧 Email Preview

**Admin ko ayega:**
```
Subject: New Contact Form Submission - [Name]

Name: John Doe
Email: john@example.com
Phone: 9876543210
Service: Hotels
Message: I need help...
```

**User ko ayega:**
```
Subject: Thank you for contacting Radrush Hospitality

Dear John,
Thank you for reaching out!
We will get back to you soon...
```

---

## ⚠️ Common Issues

**Email nahi aa raha?**
- App Password sahi hai? (16 digits)
- 2-Step Verification enabled hai?
- Spam folder check kiya?
- `python test_email.py` run karke test karein

**Authentication Error?**
- Normal password use nahi karna, App Password chahiye
- .env file save kiya?
- Server restart kiya?

---

## 📁 Files Changed

- ✅ `app.py` - Email functionality added
- ✅ `.env` - Email configuration
- ✅ `requirements.txt` - Flask-Mail added
- ✅ `static/css/style.css` - Flash message styles
- ✅ `templates/contact.html` - Already ready
- ✅ `templates/base.html` - Flash messages support

---

## 🎯 Next Steps

1. Gmail App Password generate karein
2. .env update karein
3. `python test_email.py` run karein
4. Test form submit karein
5. Done! 🎉

---

**Need Help?** Check `EMAIL_SETUP_GUIDE.md` for detailed instructions.
