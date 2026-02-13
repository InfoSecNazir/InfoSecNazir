# Smart Student Management System (SSMS) - Developer Guide

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage Guide](#usage-guide)
6. [API Documentation](#api-documentation)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Troubleshooting](#troubleshooting)

---

## System Overview

The Smart Student Management System (SSMS) is a comprehensive Django-based web application designed to manage student attendance, assignments, and performance tracking using QR code technology.

### Key Features

#### Core Features
- **Student Management**: Complete CRUD operations with automatic UUID assignment
- **QR Code Generation**: Automatic unique QR code for each student
- **Session Management**: Support for lectures, labs, exams, and assignments
- **Attendance Tracking**: Real-time QR code scanning and recording
- **Analytics Dashboard**: Comprehensive statistics and insights
- **Excel Export**: Professional attendance reports

#### Advanced Features
- **Geo-Fencing**: Location-based attendance verification (models ready)
- **Audit Logging**: Complete system activity tracking
- **Gamification**: Badge system for student motivation
- **Filtering**: Smart search and filter capabilities
- **Responsive Design**: Mobile-friendly interface

---

## Architecture

### Technology Stack

**Backend:**
- Python 3.12+
- Django 5.0+
- SQLite (development) / PostgreSQL (production recommended)

**Frontend:**
- HTML5
- Tailwind CSS 2.2.19
- JavaScript (ES6+)
- html5-qrcode library

**Libraries:**
- qrcode: QR code generation
- Pillow: Image processing
- openpyxl: Excel file handling
- reportlab: PDF generation (future)
- pyotp: TOTP for dynamic QR codes (future)

### Database Schema

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Student   │         │   Session    │         │ AttendanceLog│
├─────────────┤         ├──────────────┤         ├─────────────┤
│ id          │         │ id           │         │ id          │
│ uuid        │         │ title        │         │ student_id  │◄──┐
│ university_id│        │ session_type │         │ session_id  │◄──┤
│ name        │         │ date         │         │ status      │   │
│ email       │         │ start_time   │         │ timestamp   │   │
│ phone       │         │ end_time     │         │ latitude    │   │
│ qr_code     │         │ location     │         │ longitude   │   │
│ total_points│         │ latitude     │         │ recorded_by │   │
│ attendance_%│         │ longitude    │         │ notes       │   │
└─────────────┘         └──────────────┘         └─────────────┘
      │                                                  │
      │                                                  │
      └──────────────────────────────────────────────────┘
```

---

## Installation

### Prerequisites
```bash
# Python 3.12 or higher
python --version

# pip package manager
pip --version

# Git
git --version
```

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/InfoSecNazir/InfoSecNazir.git
cd InfoSecNazir
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply database migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Load sample data (optional)**
```bash
python populate_data.py
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL for production)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=ssms_db
DB_USER=ssms_user
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration (for notifications)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Configuration

For **Production**, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

---

## Usage Guide

### Admin Panel

1. **Navigate to** http://127.0.0.1:8000/admin/
2. **Login** with your superuser credentials

#### Managing Students

1. Go to **Students → Students**
2. Click **Add Student**
3. Fill in required fields:
   - University ID (unique)
   - Name
   - Email (unique)
   - Phone (optional)
4. Click **Save**
5. QR code is automatically generated

#### Managing Sessions

1. Go to **Students → Sessions**
2. Click **Add Session**
3. Fill in session details:
   - Title
   - Type (Lecture/Lab/Exam/Assignment)
   - Date and time
   - Location
   - Geo-fencing coordinates (optional)
4. Click **Save**

### QR Code Scanner

1. Navigate to **Scanner** from the main menu
2. Select a session from dropdown
3. Choose attendance status (Present/Late/Absent/Excused)
4. Click **Start Scanner**
5. Allow camera access
6. Scan student QR codes
7. Review recent scans below

**Manual Entry:**
- Alternatively, enter student UUID manually in the text field
- Format: `STUDENT:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### Dashboard

Access comprehensive analytics:
- Total students, sessions, and records
- At-risk students (< 50% attendance)
- Sessions by type breakdown
- Top performing students
- Recent attendance logs

### Exporting Data

1. Go to **Dashboard**
2. Click **Export to Excel**
3. Excel file downloads with:
   - Student information
   - Attendance percentages
   - Detailed statistics

---

## API Documentation

### Scan QR Code Endpoint

**URL:** `/api/scan/`  
**Method:** `POST`  
**Content-Type:** `application/json`

**Request Body:**
```json
{
  "qr_data": "STUDENT:123e4567-e89b-12d3-a456-426614174000",
  "session_id": 1,
  "status": "present",
  "latitude": 33.5138,
  "longitude": 36.2765
}
```

**Success Response:**
```json
{
  "success": true,
  "message": "Attendance recorded for Ahmad Hassan",
  "student": {
    "name": "Ahmad Hassan",
    "university_id": "CS2021001",
    "status": "present"
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Student not found"
}
```

---

## Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run with verbosity
python manage.py test --verbosity=2

# Run specific test class
python manage.py test students.tests.StudentModelTest

# Run with coverage (if installed)
coverage run manage.py test
coverage report
```

### Test Coverage

Current test coverage includes:
- ✅ Student model creation and QR generation
- ✅ Session model functionality
- ✅ Attendance log creation and uniqueness
- ✅ All view endpoints
- ✅ URL routing

### Writing New Tests

Add tests in `students/tests.py`:

```python
from django.test import TestCase
from .models import Student

class MyTestCase(TestCase):
    def setUp(self):
        # Setup test data
        self.student = Student.objects.create(
            university_id="TEST001",
            name="Test",
            email="test@example.com"
        )
    
    def test_something(self):
        # Your test logic
        self.assertEqual(self.student.name, "Test")
```

---

## Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Use PostgreSQL database
- [ ] Set up environment variables
- [ ] Configure static files with `collectstatic`
- [ ] Set up HTTPS/SSL
- [ ] Configure email backend
- [ ] Set up backup strategy
- [ ] Enable security middleware
- [ ] Configure CORS if needed

### Deployment Options

#### 1. **Heroku**

```bash
# Install Heroku CLI
heroku create ssms-app
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### 2. **DigitalOcean**

- Use App Platform or Droplet
- Configure Gunicorn and Nginx
- Set up PostgreSQL database
- Configure environment variables

#### 3. **AWS**

- Use Elastic Beanstalk or EC2
- Configure RDS for PostgreSQL
- Set up S3 for media files
- Use CloudFront for static files

---

## Troubleshooting

### Common Issues

#### 1. QR Codes Not Generating

**Problem:** QR code field is empty after creating student

**Solution:**
```bash
# Ensure Pillow is installed
pip install Pillow

# Check media directory permissions
chmod 755 media/qr_codes/
```

#### 2. Scanner Not Working

**Problem:** Camera doesn't activate

**Solution:**
- Ensure HTTPS is enabled (required for camera access)
- Check browser permissions
- Try different browser
- Use manual UUID entry as fallback

#### 3. Database Errors

**Problem:** `no such table` errors

**Solution:**
```bash
# Re-run migrations
python manage.py migrate --run-syncdb
```

#### 4. Static Files Not Loading

**Problem:** CSS/JS not appearing

**Solution:**
```bash
# Collect static files
python manage.py collectstatic

# Ensure DEBUG=True in development
# Or configure proper static file serving
```

---

## Future Enhancements

### Planned Features

1. **Dynamic QR Codes (TOTP-based)**
   - Time-based one-time passwords
   - Prevents QR code sharing

2. **Email Notifications**
   - Automatic alerts for low attendance
   - Assignment deadline reminders

3. **PWA (Progressive Web App)**
   - Offline mode support
   - Install as mobile app

4. **Advanced Analytics**
   - Machine learning predictions
   - Attendance pattern analysis

5. **Mobile App**
   - Native iOS/Android apps
   - Push notifications

6. **Integration APIs**
   - LMS integration (Moodle, Canvas)
   - University systems integration

---

## Support

For issues, questions, or contributions:

- **GitHub Issues**: https://github.com/InfoSecNazir/InfoSecNazir/issues
- **Email**: Hnzyr31@gmail.com
- **LinkedIn**: [Mohammed Nazir Al-Habash](https://www.linkedin.com/in/mohammed-nazir-al-habash-6b7385319)

---

## License

MIT License - See LICENSE file for details

---

## Credits

**Developed by:** Nazeer Al-Habash  
**Institution:** Damascus University - Computer Engineering  
**Year:** 2024

---

*Last Updated: February 2026*
