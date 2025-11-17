# 🤖 Form Automation System

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Playwright](https://img.shields.io/badge/playwright-1.40.0-brightgreen.svg)](https://playwright.dev/)
[![MongoDB](https://img.shields.io/badge/mongodb-4.0+-success.svg)](https://www.mongodb.com/)
[![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey.svg)](https://flask.palletsprojects.com/)

A powerful, enterprise-grade web form scraping and automation system built with Playwright and MongoDB. Automatically detect form fields, save templates, and fill forms with a single click.

![Form Automation System](https://via.placeholder.com/1200x400/667eea/ffffff?text=Form+Automation+System)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#️-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Database Schema](#️-database-schema)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Security](#-security)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Support](#-support)

---

## ✨ Features

### Core Features
- 🔍 **Real-Time Web Scraping** - Extract form fields from any website using Playwright browser automation
- 💾 **MongoDB Integration** - Persistent storage with robust database management
- 🚀 **Automated Form Filling** - One-click form completion with visual browser automation
- 📸 **Screenshot Capture** - Automatic screenshots during scraping and form submission
- 📊 **Activity Logging** - Comprehensive audit trail of all operations
- 🎨 **Modern UI** - Beautiful gradient interface with real-time status indicators

### Advanced Features
- ✅ Intelligent field detection (input, textarea, select, checkbox, radio)
- ✅ Automatic CSS selector generation
- ✅ Required field identification
- ✅ Label and placeholder extraction
- ✅ Select dropdown option detection
- ✅ Error handling and recovery
- ✅ Timeout management
- ✅ Form template management
- ✅ RESTful API endpoints
- ✅ Real-time system health monitoring

---

## 🎥 Demo

### Scraping a Form
![Scraping Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Scraping+Demo)

### Filling a Form
![Filling Demo](https://via.placeholder.com/800x400/764ba2/ffffff?text=Filling+Demo)

### Live Demo
🌐 [View Live Demo](https://your-demo-url.com) *(Coming Soon)*

---

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Flask** | Web Framework | 3.0.0 |
| **Playwright** | Browser Automation | 1.40.0 |
| **MongoDB** | Database | 4.0+ |
| **PyMongo** | MongoDB Driver | 4.6.1 |
| **Python** | Backend Language | 3.8+ |
| **HTML5/CSS3** | Frontend | Latest |
| **JavaScript** | Frontend Logic | ES6+ |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- ✅ **Python 3.8 or higher**
  ```bash
  python --version
  ```

- ✅ **MongoDB 4.0 or higher**
  ```bash
  mongod --version
  ```

- ✅ **pip** (Python package manager)
  ```bash
  pip --version
  ```

- ✅ **Git** (for cloning repository)
  ```bash
  git --version
  ```

---

## 🚀 Installation

### Method 1: Automated Setup (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/form-automation-system.git
cd form-automation-system

# 2. Run automated setup
python setup.py
```

This will automatically:
- Install all Python dependencies
- Install Playwright browsers
- Check MongoDB connection
- Create project structure

### Method 2: Manual Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/form-automation-system.git
cd form-automation-system

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install Playwright browsers
playwright install chromium

# 6. Create .env file
echo "MONGO_URI=mongodb://localhost:27017/" > .env
```

---

## 🏃 Quick Start

### Step 1: Start MongoDB

**Windows:**
```cmd
net start MongoDB
```

**Linux:**
```bash
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

**macOS:**
```bash
brew services start mongodb-community
```

### Step 2: Run Application

```bash
python app.py
```

You should see:
```
============================================================
🤖 Form Automation System
============================================================
MongoDB: mongodb://localhost:27017/
Server: http://localhost:5000
============================================================
 * Running on http://0.0.0.0:5000
```

### Step 3: Open Browser

Navigate to: **http://localhost:5000**

### Step 4: Test the System

1. ✅ Check status indicators (green = working)
2. ✅ Try scraping: `https://www.w3schools.com/html/html_forms.asp`
3. ✅ Save the form template
4. ✅ Fill the form with test data

---

## 📖 Usage Guide

### 1. Scraping a Form

#### Step-by-Step:

1. **Navigate to "🔍 Scrape Form" tab**

2. **Enter Form Details:**
   - **Form Name:** Give your form a memorable name (e.g., "Contact Form")
   - **Target URL:** Enter the complete URL (e.g., `https://example.com/contact`)

3. **Click "🔍 Scrape Form Fields"**
   - Playwright will open the page
   - Extract all form fields automatically
   - Display screenshot preview

4. **Review Fields:**
   - Check detected fields
   - Edit CSS selectors if needed
   - Verify field types

5. **Click "💾 Save Form Template"**
   - Form saved to MongoDB
   - Ready for automated filling

#### Example:
```
Form Name: Newsletter Signup
URL: https://example.com/newsletter
Fields Detected: email, name, subscribe_button
```

### 2. Managing Forms

#### View Saved Forms:

1. Go to **"📋 Manage Forms"** tab
2. See all saved form templates
3. View details:
   - Form name
   - Target URL
   - Number of fields
   - Creation date

#### Delete Forms:

1. Click **"🗑️ Delete"** button
2. Confirm deletion
3. Form removed from database

### 3. Filling Forms

#### Automated Form Filling:

1. **Navigate to "✍️ Fill Form" tab**

2. **Select Form:**
   - Choose from saved templates dropdown

3. **Enter Values:**
   - Fill in values for each field
   - Required fields marked with *

4. **Click "🚀 Auto-Fill Form"**
   - Browser opens automatically
   - Fields filled in real-time
   - Submit button clicked
   - Screenshot captured

#### Example Session:
```
Selected Form: Contact Form
Fields to Fill:
  - Name: John Doe
  - Email: john@example.com
  - Message: Hello, this is automated!

Result: ✅ Form filled successfully (3 fields)
```

### 4. Viewing Logs

#### Activity Logs:

1. Go to **"📊 Logs"** tab
2. View all operations:
   - Scraping activities
   - Form fills
   - Errors and successes
   - Timestamps

#### Log Filters:
- ✅ Success operations (green)
- ❌ Failed operations (red)
- 📝 All activities sorted by time

#### Clear Logs:
- Click **"🗑️ Clear All"** to remove all logs
- Useful for maintenance

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Get All Forms
```http
GET /api/forms
```

**Response:**
```json
{
  "status": "success",
  "forms": [
    {
      "form_id": "1699876543210",
      "name": "Contact Form",
      "url": "https://example.com/contact",
      "fields": [...],
      "created_at": "2024-11-17T10:30:00"
    }
  ]
}
```

#### 2. Create Form
```http
POST /api/forms
Content-Type: application/json

{
  "form_id": "unique_id",
  "name": "Form Name",
  "url": "https://example.com",
  "fields": [...]
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Form saved successfully"
}
```

#### 3. Delete Form
```http
DELETE /api/forms/{form_id}
```

**Response:**
```json
{
  "status": "success",
  "message": "Form deleted"
}
```

#### 4. Scrape Form
```http
POST /api/scrape
Content-Type: application/json

{
  "url": "https://example.com/form"
}
```

**Response:**
```json
{
  "status": "success",
  "fields": [...],
  "screenshot": "base64_encoded_image",
  "count": 5
}
```

#### 5. Fill Form
```http
POST /api/fill
Content-Type: application/json

{
  "form_id": "1699876543210",
  "values": {
    "email": "test@example.com",
    "name": "John Doe"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Form filled successfully",
  "filled_fields": ["email", "name"],
  "errors": [],
  "screenshot": "base64_encoded_image"
}
```

#### 6. Get Logs
```http
GET /api/logs
```

**Response:**
```json
{
  "status": "success",
  "logs": [
    {
      "form_id": "1699876543210",
      "action": "fill",
      "status": "success",
      "message": "Filled 3 fields",
      "timestamp": "2024-11-17T10:35:00"
    }
  ]
}
```

#### 7. Clear Logs
```http
DELETE /api/logs
```

#### 8. Test System
```http
GET /api/test-connection
```

**Response:**
```json
{
  "mongodb": true,
  "playwright": true,
  "timestamp": "2024-11-17T10:30:00"
}
```

---

## 🗄️ Database Schema

### Forms Collection

```javascript
{
  _id: ObjectId("..."),
  form_id: "1699876543210",              // Unique identifier
  name: "Contact Form",                   // Form name
  url: "https://example.com/contact",     // Target URL
  fields: [
    {
      name: "email",                      // Field name
      type: "email",                      // Input type
      selector: "#email",                 // CSS selector
      label: "Email Address",             // Associated label
      placeholder: "Enter your email",    // Placeholder text
      required: true,                     // Required flag
      tagName: "input"                    // HTML tag
    },
    {
      name: "message",
      type: "textarea",
      selector: "#message",
      label: "Your Message",
      placeholder: "Type message here",
      required: false,
      tagName: "textarea"
    }
  ],
  created_at: "2024-11-17T10:30:00"      // Creation timestamp
}
```

### Logs Collection

```javascript
{
  _id: ObjectId("..."),
  form_id: "1699876543210",              // Reference to form
  timestamp: "2024-11-17T10:35:00",      // Operation time
  action: "fill",                         // Action type: scrape/fill/delete
  status: "success",                      // Status: success/error
  message: "Filled 3 fields",            // Description
  filled_fields: ["email", "name"],      // Successfully filled
  errors: [],                             // Any errors encountered
  values: {                               // Submitted values
    email: "test@example.com",
    name: "John Doe"
  }
}
```

### Database Indexes

```python
# Automatically created on startup
forms_collection.create_index('form_id', unique=True)
logs_collection.create_index('timestamp')
```

---

## ⚙️ Configuration

### Environment Variables

Create `.env` file:

```env
# MongoDB Connection
MONGO_URI=mongodb://localhost:27017/

# For MongoDB Atlas (cloud):
# MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/formdb?retryWrites=true&w=majority

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Server Configuration
HOST=0.0.0.0
PORT=5000
```

### Application Settings

Edit `app.py`:

```python
# Server Configuration
app.run(
    debug=True,           # Enable debug mode
    host='0.0.0.0',       # Listen on all interfaces
    port=5000             # Port number
)

# MongoDB Configuration
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['form_automation']  # Database name
```

### Playwright Settings

```python
# Browser Configuration
browser = p.chromium.launch(
    headless=False,       # Visible browser (True for headless)
    slow_mo=50            # Slow down operations (milliseconds)
)

# Page Timeout
page.goto(url, 
    wait_until='networkidle',  # Wait for network idle
    timeout=30000               # 30 seconds timeout
)
```

---

## 📁 Project Structure

```
form-automation-system/
│
├── 📄 app.py                    # Flask application & API routes
├── 📄 setup.py                  # Automated setup script
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env                      # Environment variables
├── 📄 .gitignore               # Git ignore rules
├── 📄 README.md                # This file
├── 📄 QUICKSTART.md            # Quick start guide
├── 📄 LICENSE                  # MIT License
│
├── 📁 templates/
│   └── 📄 index.html           # Web interface (single-page app)
│
├── 📁 static/                  # Static assets (optional)
│   ├── 📁 css/
│   ├── 📁 js/
│   └── 📁 images/
│
├── 📁 venv/                    # Virtual environment (not committed)
│
└── 📁 logs/                    # Application logs (optional)
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. MongoDB Connection Error

**Error:**
```
pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [Errno 111] Connection refused
```

**Solution:**
```bash
# Check if MongoDB is running
# Windows:
net start MongoDB

# Linux:
sudo systemctl status mongodb
sudo systemctl start mongodb

# Mac:
brew services list
brew services start mongodb-community

# Verify connection
mongosh
```

#### 2. Playwright Installation Issues

**Error:**
```
playwright._impl._api_types.Error: Executable doesn't exist
```

**Solution:**
```bash
# Reinstall Playwright
pip uninstall playwright
pip install playwright==1.40.0

# Install browsers
playwright install chromium

# Or with Python
python -m playwright install chromium
```

#### 3. Port Already in Use

**Error:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**
```bash
# Find process using port 5000
# Windows:
netstat -ano | findstr :5000

# Linux/Mac:
lsof -i :5000

# Kill the process or change port in app.py
app.run(port=5001)
```

#### 4. Scraping Timeout

**Error:**
```
playwright._impl._api_types.TimeoutError: Timeout 30000ms exceeded
```

**Solution:**
```python
# Increase timeout in app.py
page.goto(url, wait_until='networkidle', timeout=60000)  # 60 seconds

# Or try different wait condition
page.goto(url, wait_until='load', timeout=30000)
```

#### 5. Permission Denied (Linux/Mac)

**Error:**
```
PermissionError: [Errno 13] Permission denied
```

**Solution:**
```bash
# Install with user flag
pip install --user -r requirements.txt

# Or use sudo (not recommended)
sudo pip install -r requirements.txt

# Fix permissions
sudo chown -R $USER:$USER ~/.local
```

#### 6. ModuleNotFoundError

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Activate virtual environment first
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Then install
pip install -r requirements.txt
```

### Getting Help

If issues persist:

1. 📖 Check [QUICKSTART.md](QUICKSTART.md)
2. 🔍 Search existing GitHub issues
3. 🐛 Create new issue with:
   - Error message
   - Python version
   - OS details
   - Steps to reproduce
4. 💬 Contact: your.email@example.com

---

## 🔐 Security

### Important Security Notes

⚠️ **This application is designed for local/internal use only**

#### Production Deployment Checklist

- [ ] Add authentication (JWT, OAuth, or basic auth)
- [ ] Enable HTTPS/TLS
- [ ] Set `debug=False` in production
- [ ] Use environment variables for secrets
- [ ] Implement rate limiting
- [ ] Add CORS restrictions
- [ ] Sanitize user inputs
- [ ] Enable MongoDB authentication
- [ ] Use firewall rules
- [ ] Regular security updates

#### Best Practices

```python
# ❌ Don't do this in production
app.run(debug=True, host='0.0.0.0', port=5000)

# ✅ Do this instead
app.run(debug=False, host='127.0.0.1', port=5000)
```

#### Data Privacy

- 🔒 Never store passwords or sensitive data
- 🛡️ Use environment variables for credentials
- 🚫 Don't commit `.env` file to Git
- 🔑 Implement proper access controls
- 📝 Follow GDPR/privacy regulations

#### Web Scraping Ethics

- ✅ Respect robots.txt
- ✅ Check Terms of Service
- ✅ Add delays between requests
- ✅ Use appropriate User-Agent
- ✅ Don't overload servers
- ⚖️ Comply with legal requirements

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest features
- 📖 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repository
- 📢 Spread the word

### Development Setup

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/form-automation-system.git

# 3. Create feature branch
git checkout -b feature/amazing-feature

# 4. Make your changes
# 5. Test thoroughly

# 6. Commit with meaningful message
git commit -m "Add amazing feature"

# 7. Push to your fork
git push origin feature/amazing-feature

# 8. Open Pull Request
```

### Coding Standards

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions
- Write unit tests
- Update documentation

### Pull Request Guidelines

- ✅ Clear description of changes
- ✅ Link to related issues
- ✅ Test on multiple browsers
- ✅ Update README if needed
- ✅ No breaking changes

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Web scraping with Playwright
- ✅ MongoDB storage
- ✅ Automated form filling
- ✅ Activity logging
- ✅ Screenshot capture

### Version 1.1 (Coming Soon)
- ⏳ User authentication
- ⏳ Form scheduling
- ⏳ Export/Import templates
- ⏳ Dark mode UI
- ⏳ Browser selection (Firefox, WebKit)

### Version 2.0 (Future)
- 🔮 Cloud deployment support
- 🔮 Multi-user support
- 🔮 Form validation rules
- 🔮 Webhook notifications
- 🔮 Advanced analytics
- 🔮 Mobile app

### Feature Requests

Have an idea? [Open an issue](https://github.com/yourusername/form-automation-system/issues/new) with the "enhancement" label!

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
