# 🚀 Quick Reference - Email Setup

## ⚡ 3-Minute Setup

### 1. Generate App Password (2 minutes)
```
1. Login: radrushmarketing@gmail.com
2. Visit: https://myaccount.google.com/apppasswords
3. Create: Mail → Other → "Radrush Website"
4. Copy: 16-digit password
```

### 2. Update .env (30 seconds)
```env
MAIL_PASSWORD=xxxx xxxx xxxx xxxx
```

### 3. Test & Run (30 seconds)
```bash
pip install Flask-Mail
python test_email.py
python run.py
```

---

## 📧 Email Addresses

**Company Email:** radrushmarketing@gmail.com
- ✅ Receives all contact form submissions
- ✅ Sends confirmation emails to users
- ✅ Already configured in code

---

## 🧪 Testing Commands

```bash
# Test email configuration
python test_email.py

# Run server
python run.py

# Test URL
http://localhost:5000/contact
```

---

## 📨 What Happens

```
User submits form
    ↓
radrushmarketing@gmail.com gets notification
    ↓
User gets confirmation email
    ↓
Saved in database
```

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Authentication failed | Use App Password, not regular password |
| Email not received | Check spam folder |
| Connection error | Check internet connection |
| Import error | Run `pip install Flask-Mail` |

---

## 📁 Important Files

- `app.py` - Main application (email code here)
- `.env` - Configuration (add App Password here)
- `test_email.py` - Test script
- `RADRUSH_EMAIL_SETUP.md` - Detailed guide
- `EMAIL_FLOW_DIAGRAM.md` - Visual flow

---

## ✅ Checklist

- [ ] App Password generated
- [ ] .env updated
- [ ] Flask-Mail installed
- [ ] Test email successful
- [ ] Form submission tested
- [ ] Admin email received
- [ ] User confirmation received

---

## 🎯 Current Status

**Email:** radrushmarketing@gmail.com ✅  
**Configuration:** Complete ✅  
**Code:** Ready ✅  
**Needed:** App Password only! 🔑

---

## 📞 Quick Help

**Can't generate App Password?**
- Enable 2-Step Verification first
- Use Google Account, not Gmail app

**Email not sending?**
- Run: `python test_email.py`
- Check error message
- Verify .env file saved

**Form not working?**
- Check server is running
- Visit: http://localhost:5000/contact
- Check browser console for errors

---

## 🎉 That's It!

Sirf App Password chahiye, baaki sab ready hai! 🚀
