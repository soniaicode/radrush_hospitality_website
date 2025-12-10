# 📧 Radrush Email Setup - radrushmarketing@gmail.com

## ✅ Current Configuration

Aapki company email **radrushmarketing@gmail.com** already configured hai!

**Kya hoga:**
- User form submit karega → **radrushmarketing@gmail.com** par notification ayega
- User ko automatic confirmation email jayega
- Database mein save hoga

---

## 🚀 Setup (Sirf 1 Step!)

### Gmail App Password Generate Karein

Aapko **radrushmarketing@gmail.com** ke liye App Password chahiye:

#### Step-by-Step:

1. **Gmail Account Login** karein: radrushmarketing@gmail.com

2. **Google Account Settings** kholen:
   - https://myaccount.google.com/

3. **Security** section mein jayein

4. **2-Step Verification** enable karein (agar already nahi hai)
   - Agar already enabled hai, next step par jayein

5. **App Passwords** search karein
   - Search box mein "App Passwords" type karein
   - Ya direct link: https://myaccount.google.com/apppasswords

6. **Generate Password:**
   - Select app: **Mail**
   - Select device: **Other (Custom name)**
   - Name: "Radrush Website" ya "Contact Form"
   - Click **Generate**

7. **16-digit Password** copy karein
   - Format: `xxxx xxxx xxxx xxxx`
   - Ye password sirf ek baar dikhega

8. **.env File Update** karein:
   ```env
   MAIL_PASSWORD=xxxx xxxx xxxx xxxx
   ```
   - Spaces rakh sakte hain ya hata sakte hain, dono chalega

---

## 🧪 Testing

### Step 1: Install Dependencies
```bash
pip install Flask-Mail
```

### Step 2: Test Email Configuration
```bash
python test_email.py
```

Ye script:
- ✅ Configuration check karega
- ✅ Test email bhejega radrushmarketing@gmail.com par
- ✅ Errors show karega agar koi problem ho

### Step 3: Run Server
```bash
python run.py
```

### Step 4: Test Contact Form
1. Browser mein kholen: http://localhost:5000/contact
2. Form fill karein
3. Submit karein
4. Check karein:
   - ✅ radrushmarketing@gmail.com inbox
   - ✅ User email inbox (jo aapne form mein dala)
   - ✅ Success message website par

---

## 📧 Email Preview

### Admin Email (radrushmarketing@gmail.com ko ayega):

**Subject:** New Contact Form Submission - [User Name]

**Content:**
```
New Contact Form Submission

Name: John Doe
Email: john@example.com
Phone: 9876543210
Service Interested: Hotels

Message:
I need help with hotel marketing...

Submitted at: 2024-12-02 10:30:45 UTC
```

### User Confirmation Email:

**Subject:** Thank you for contacting Radrush Hospitality

**Content:**
```
Dear John,

Thank you for reaching out to Radrush Hospitality!

We have received your message and will get back to you soon.

Your submitted details:
- Name: John Doe
- Email: john@example.com
- Phone: 9876543210
- Service: Hotels

Best regards,
Radrush Hospitality Team
Phone: 7056456555
Email: radrushmarketing@gmail.com
```

---

## ⚠️ Troubleshooting

### Email Nahi Aa Raha?

**1. Check App Password:**
```bash
python test_email.py
```
- Agar "Authentication failed" dikhe → App Password galat hai
- Agar "Success" dikhe → Configuration sahi hai

**2. Check Gmail Settings:**
- 2-Step Verification enabled hai?
- App Password correctly generate kiya?
- Correct email use kar rahe ho? (radrushmarketing@gmail.com)

**3. Check Spam Folder:**
- Pehli baar emails spam mein ja sakte hain
- "Not Spam" mark kar dein

**4. Check .env File:**
```env
MAIL_USERNAME=radrushmarketing@gmail.com
MAIL_PASSWORD=xxxx xxxx xxxx xxxx    # 16 digits
ADMIN_EMAIL=radrushmarketing@gmail.com
```

**5. Server Restart:**
```bash
# Stop current server (Ctrl+C)
python run.py
```

---

## 🔒 Security Tips

1. **App Password** kabhi share na karein
2. **.env file** Git mein commit na karein (already .gitignore mein hai)
3. **Regular password** use na karein, sirf App Password
4. Agar password leak ho jaye, turant revoke karein aur naya generate karein

---

## 📊 Email Management

### Inbox Organization:

**Gmail Labels** create kar sakte hain:
1. Gmail Settings → Labels
2. New label: "Website Contacts"
3. Filter create karein:
   - Subject contains: "New Contact Form Submission"
   - Apply label: "Website Contacts"

### Auto-Reply Setup (Optional):

Agar aap chahte hain ki automatic reply bhi jaye:
- Gmail Settings → Vacation responder
- Ya code already user ko confirmation email bhej raha hai

---

## 🎯 Quick Commands

```bash
# Install dependencies
pip install Flask-Mail

# Test email
python test_email.py

# Run server
python run.py

# Check if server is running
# Open: http://localhost:5000/contact
```

---

## ✨ Features Active

- ✅ Admin notification to radrushmarketing@gmail.com
- ✅ User confirmation email
- ✅ Beautiful HTML email templates
- ✅ Database backup (MongoDB)
- ✅ Error handling
- ✅ Flash messages on website
- ✅ Mobile responsive
- ✅ Form validation

---

## 📞 Next Steps

1. **Generate App Password** for radrushmarketing@gmail.com
2. **Update .env** with the password
3. **Run test:** `python test_email.py`
4. **Start server:** `python run.py`
5. **Test form:** http://localhost:5000/contact

---

## 🎉 Ready!

Bas App Password set karein aur test karein. Sab kuch ready hai!

**Email:** radrushmarketing@gmail.com ✅  
**Configuration:** Complete ✅  
**Code:** Ready ✅  

Sirf App Password chahiye! 🚀
