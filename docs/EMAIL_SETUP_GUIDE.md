# Email Setup Guide - Contact Form

## ✅ Kya Ho Gaya Hai

Contact form ab email functionality ke saath ready hai! Jab bhi koi user contact form fill karega:

1. **Admin ko email jayega** - User ki saari details ke saath
2. **User ko confirmation email jayega** - Thank you message ke saath
3. **Database mein save hoga** - MongoDB mein record store hoga

## 📧 Email Setup Kaise Karein

### Step 1: Gmail App Password Banayein

Gmail se email bhejne ke liye aapko **App Password** chahiye (normal password nahi chalega):

1. **Google Account Settings** mein jayein: https://myaccount.google.com/
2. **Security** section mein jayein
3. **2-Step Verification** enable karein (agar already nahi hai)
4. **App Passwords** search karein
5. **Select app**: Mail
6. **Select device**: Other (Custom name) - "Radrush Website" likh dein
7. **Generate** button click karein
8. 16-digit password copy kar lein

### Step 2: .env File Update Karein

`.env` file mein ye values update karein:

```env
# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=radrushmarketing@gmail.com
MAIL_PASSWORD=xxxx xxxx xxxx xxxx    # Yahan 16-digit App Password paste karein
ADMIN_EMAIL=radrushmarketing@gmail.com
```

**Important:** 
- `MAIL_PASSWORD` mein wo 16-digit App Password paste karein jo aapne generate kiya
- Spaces hata dein ya rakh dein, dono chalega

### Step 3: Flask-Mail Install Karein

```bash
pip install Flask-Mail
```

Ya phir:

```bash
pip install -r requirements.txt
```

### Step 4: Server Restart Karein

```bash
python run.py
```

## 🎯 Kaise Kaam Karta Hai

### Jab User Form Submit Karta Hai:

1. **Database Save**: User details MongoDB mein save hoti hain
2. **Admin Email**: Aapko (radrushmarketing@gmail.com) email jayega with:
   - User ka naam
   - User ka email
   - Phone number
   - Service interest
   - Message
   - Submission time

3. **User Confirmation**: User ko thank you email jayega

### Email Format

**Admin ko:**
```
Subject: New Contact Form Submission - [User Name]

Name: John Doe
Email: john@example.com
Phone: 9876543210
Service: Hotels
Message: I need help with hotel marketing...
```

**User ko:**
```
Subject: Thank you for contacting Radrush Hospitality

Dear John,

Thank you for reaching out to Radrush Hospitality!
We have received your message and will get back to you soon.

Your submitted details:
- Name: John Doe
- Email: john@example.com
...
```

## 🔧 Testing

1. Website kholen: http://localhost:5000/contact
2. Form fill karein
3. Submit karein
4. Check karein:
   - Admin email (radrushmarketing@gmail.com) mein notification aaya?
   - User email mein confirmation aaya?
   - Success message dikha website par?

## ⚠️ Troubleshooting

### Email Nahi Aa Raha?

1. **Check App Password**: 
   - Sahi 16-digit password use kiya?
   - Spaces remove kar diye?

2. **Check Gmail Settings**:
   - 2-Step Verification enabled hai?
   - App Password correctly generate kiya?

3. **Check Spam Folder**: 
   - Pehli baar emails spam mein ja sakte hain

4. **Check Console Logs**:
   - Terminal mein error messages check karein
   - "Email sending error" dikha to kya error hai?

### Common Errors:

**"Authentication failed"**
- Wrong App Password
- 2-Step Verification not enabled
- Using normal password instead of App Password

**"Connection refused"**
- Internet connection check karein
- Firewall settings check karein

**"Sender address rejected"**
- MAIL_USERNAME sahi email hai?
- Email verified hai?

## 📝 Alternative Email Services

Agar Gmail nahi use karna chahte:

### Outlook/Hotmail:
```env
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@outlook.com
MAIL_PASSWORD=your-password
```

### Yahoo:
```env
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@yahoo.com
MAIL_PASSWORD=your-app-password
```

### SendGrid (Professional):
```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=apikey
MAIL_PASSWORD=your-sendgrid-api-key
```

## 🎨 Email Customization

Email templates customize karne ke liye `app.py` mein `contact()` function edit karein:

- **Subject line** change kar sakte hain
- **Email body** HTML/text customize kar sakte hain
- **Colors** change kar sakte hain
- **Logo** add kar sakte hain

## 📊 Database Records

Saare contact form submissions MongoDB mein save hote hain:

```python
# View all contacts
mongo.db.contacts.find()

# View new contacts only
mongo.db.contacts.find({'status': 'new'})
```

## ✨ Features

- ✅ Admin ko instant email notification
- ✅ User ko automatic confirmation email
- ✅ Beautiful HTML email templates
- ✅ Database mein permanent record
- ✅ Error handling agar email fail ho
- ✅ Form validation
- ✅ Success/error messages

## 🚀 Production Tips

Production mein deploy karte waqt:

1. **Environment Variables** secure rakhein
2. **App Password** kabhi code mein hardcode na karein
3. **Rate limiting** add karein (spam prevention)
4. **Email queue** use karein (Celery/Redis)
5. **Professional email service** use karein (SendGrid, AWS SES)

## 📞 Support

Koi problem ho to:
- Terminal logs check karein
- .env file verify karein
- Gmail App Password re-generate karein
- Internet connection check karein

---

**Ready to test!** 🎉

Form submit karein aur dekhen emails aa rahe hain ya nahi!
