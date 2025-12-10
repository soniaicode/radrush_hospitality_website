# 🔐 Admin Dashboard Credentials

## Admin Login Details

**Dashboard URL:** `http://your-domain.com/admin/login`

**Username:** `radrush_admin`

**Password:** `Radrush@2024`

---

## 📊 Admin Dashboard Features

### 1. **Statistics Cards**
- Total Contacts
- Today's Contacts
- This Week's Contacts
- This Month's Contacts

### 2. **Filters**
- **Date Range Filter:** From Date to To Date
- **Service Filter:** Filter by specific service (Hotels, Resorts, Gyms, etc.)
- Apply filters to see specific contacts

### 3. **Contact Table**
View all contact submissions with:
- Date & Time
- Name
- Email
- Phone
- Service
- Message
- Status (new/contacted)

### 4. **Export Feature**
- Export all contacts to CSV file
- Download button available
- File name: `contacts_YYYY-MM-DD.csv`

---

## 🔒 Security Features

- Password is hashed using SHA-256
- Session-based authentication
- Login required for dashboard access
- Automatic logout functionality
- All login attempts logged

---

## 📝 How to Use

### Login:
1. Go to `/admin/login`
2. Enter username: `radrush_admin`
3. Enter password: `Radrush@2024`
4. Click Login

### View Contacts:
1. After login, you'll see the dashboard
2. View statistics at the top
3. Scroll down to see all contacts

### Filter Contacts:
1. Select "From Date" and "To Date"
2. Choose a service (optional)
3. Click "Apply Filters"

### Export Data:
1. Click "Export to CSV" button
2. File will download automatically
3. Open in Excel or Google Sheets

### Logout:
1. Click "Logout" button in top right
2. You'll be redirected to login page

---

## 🔧 Change Admin Password

To change the admin password:

1. Open `.env` file
2. Update `ADMIN_PASSWORD=YourNewPassword`
3. Restart the application

**Example:**
```env
ADMIN_USERNAME=radrush_admin
ADMIN_PASSWORD=MyNewSecurePassword123
```

---

## 📱 Access URLs

- **Login:** `/admin/login`
- **Dashboard:** `/admin/dashboard`
- **Logout:** `/admin/logout`

---

## ⚠️ Important Notes

1. **Keep credentials secure** - Don't share with unauthorized users
2. **Change default password** - Update password in production
3. **Use HTTPS** - Always use secure connection in production
4. **Regular backups** - Backup MongoDB database regularly
5. **Monitor logs** - Check `logs/contact_submissions.log` for activity

---

## 🚀 Quick Start

```bash
# Start the application
python app.py

# Open browser
http://localhost:5000/admin/login

# Login with credentials
Username: radrush_admin
Password: Radrush@2024
```

---

**Created for:** Radrush Hospitality
**Last Updated:** December 2024
