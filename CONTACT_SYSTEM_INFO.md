# Contact System - Complete Information

## 📧 Email Flow

### When someone fills the contact form:

1. **User fills form** with:
   - Name
   - Email
   - Phone (optional)
   - Service interested in
   - Message

2. **System saves to MongoDB database** ✅
   - All contact details stored
   - Timestamp added
   - Status: "new"

3. **Email sent to Admin** (radrushmarketing@gmail.com) ✅
   - Subject: "New Contact Form Submission - [Name]"
   - Contains all user details
   - Beautiful HTML formatted email

4. **Confirmation email sent to User** ✅
   - Thank you message
   - Copy of their submitted details
   - Contact information of Radrush team

5. **Logged to file** ✅
   - All actions logged in `logs/contact_submissions.log`
   - Includes timestamps and details

## 📊 Database Storage

**Collection:** `contacts`

**Fields stored:**
```json
{
  "name": "User Name",
  "email": "user@example.com",
  "phone": "+91 1234567890",
  "service": "hotels",
  "message": "User message here",
  "created_at": "2024-12-10T10:30:00Z",
  "status": "new"
}
```

## 📝 Logging System

**Log File:** `logs/contact_submissions.log`

**What gets logged:**
- ✅ New contact saved with database ID
- ✅ Admin email sent confirmation
- ✅ User confirmation email sent
- ❌ Any errors that occur

**Log Features:**
- Rotating files (max 10MB each)
- Keeps last 10 backup files
- Automatic timestamps
- Error tracking

## 🔧 Configuration Required

**In .env file:**
```env
MAIL_USERNAME=radrushmarketing@gmail.com
MAIL_PASSWORD=your-gmail-app-password
ADMIN_EMAIL=radrushmarketing@gmail.com
MONGO_URI=your-mongodb-connection-string
```

## 📱 API Endpoints

### Get all contacts:
```
GET /api/contacts
```
Returns all contact submissions from database

### Get statistics:
```
GET /api/stats
```
Returns total contacts, new contacts, etc.

## ✅ Summary

**YES, everything works as you requested:**
1. ✅ User submits contact form
2. ✅ Admin receives email at radrushmarketing@gmail.com
3. ✅ User receives confirmation email
4. ✅ All details saved in MongoDB database
5. ✅ Everything logged in log file

**All set and ready to use!** 🚀
