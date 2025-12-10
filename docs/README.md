# Radrush Hospitality Website

A professional Flask-based website for Radrush Hospitality - providing free promotional services for hotels, resorts, gyms, clubs, pubs, and wedding planners.

## Features

- 🎨 Modern, responsive design
- 🚀 Flask backend with MongoDB integration
- 📧 Contact form with database storage
- 🔄 Jinja2 templating
- 📱 Mobile-friendly navigation
- ✨ Smooth animations and transitions
- 🎯 Service-specific pages

## Tech Stack

- **Backend**: Flask 3.0
- **Database**: MongoDB
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Jinja2
- **Icons**: Font Awesome 6.4

## Project Structure

```
radrush_hospitality_website/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── static/                # Static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
└── templates/             # Jinja2 templates
    ├── base.html          # Base template
    ├── index.html         # Home page
    ├── about.html         # About page
    ├── contact.html       # Contact page
    └── services/          # Service pages
        ├── index.html
        ├── hotels.html
        ├── resorts.html
        ├── gyms.html
        ├── clubs-pubs.html
        └── wedding-planning.html
```

## Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB (local or MongoDB Atlas)
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   - Open `.env` file
   - Update MongoDB URI:
     ```
     MONGO_URI=mongodb://localhost:27017/radrush_hospitality
     ```
   - Or use MongoDB Atlas:
     ```
     MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/radrush_hospitality
     ```
   - Change SECRET_KEY to a secure random string

6. **Start MongoDB** (if using local MongoDB)
   ```bash
   mongod
   ```

7. **Run the application**
   ```bash
   python app.py
   ```

8. **Open in browser**
   ```
   http://localhost:5000
   ```

## MongoDB Setup

### Local MongoDB

1. Install MongoDB from https://www.mongodb.com/try/download/community
2. Start MongoDB service
3. Database and collections will be created automatically

### MongoDB Atlas (Cloud)

1. Create account at https://www.mongodb.com/cloud/atlas
2. Create a cluster
3. Get connection string
4. Update MONGO_URI in `.env` file

## Database Collections

### contacts
Stores contact form submissions:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+91 1234567890",
  "service": "hotels",
  "message": "Interested in hotel promotion",
  "created_at": "2024-12-01T10:30:00",
  "status": "new"
}
```

## API Endpoints

- `GET /` - Home page
- `GET /about` - About page
- `GET /services` - Services overview
- `GET /services/hotels` - Hotel services
- `GET /services/resorts` - Resort services
- `GET /services/gyms` - Gym services
- `GET /services/clubs-pubs` - Clubs & Pubs services
- `GET /services/wedding-planning` - Wedding planning services
- `GET /contact` - Contact page
- `POST /contact` - Submit contact form
- `GET /api/contacts` - Get all contacts (JSON)
- `GET /api/stats` - Get statistics (JSON)

## Customization

### Update Logo
Replace `static/images/logo.png` with your logo

### Update Contact Information
Edit `templates/contact.html` and update:
- Phone number
- Email address
- Physical address

### Update Colors
Edit `static/css/style.css` and modify CSS variables:
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
    --accent-color: #3b82f6;
}
```

## Deployment

### Heroku
```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
```

### PythonAnywhere
1. Upload files
2. Create virtual environment
3. Configure WSGI file
4. Set environment variables

### Render
1. Connect GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`
4. Add environment variables

## Development

To run in development mode:
```bash
export FLASK_ENV=development  # Mac/Linux
set FLASK_ENV=development     # Windows
python app.py
```

## Support

For issues or questions, contact: [email]@radrushhospitality.com

## License

© 2024 Radrush Hospitality. All rights reserved.
