# PythonAnywhere Deployment Guide

## Prerequisites
- PythonAnywhere account (free tier works)
- GitHub repository: `nadeemmaahmud/LoveConnect`

## Step 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com/
2. Sign up for a free Beginner account
3. Confirm your email

## Step 2: Open Bash Console
1. Go to **Dashboard** → **Consoles** tab
2. Click **"Bash"** to start a new console

## Step 3: Clone Your Repository
```bash
git clone https://github.com/nadeemmaahmud/LoveConnect.git
cd LoveConnect
```

## Step 4: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.11 datingapp
```

Or if that doesn't work:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

## Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 6: Configure Environment Variables
Create a `.env` file in the project root:
```bash
nano .env
```

Add these variables:
```bash
SECRET_KEY=#2lth^f$hu&bld7x76ihltzx=c)q%a2qenc^5q+6pgat&&xg61
DEBUG=False
PYTHONANYWHERE_DOMAIN=YOUR_USERNAME.pythonanywhere.com
CLOUDINARY_CLOUD_NAME=dmdjz28ru
CLOUDINARY_API_KEY=482843432266249
CLOUDINARY_API_SECRET=72h8xldIO8hDwDgopJ9M_67CzxI
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

Save with `Ctrl+O`, `Enter`, then exit with `Ctrl+X`.

## Step 7: Load Environment Variables
Add to the end of `Dating_Website/settings.py`:
```python
# Load .env file if it exists
from pathlib import Path
env_file = BASE_DIR / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key, value)
```

## Step 8: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

## Step 9: Run Migrations
```bash
python manage.py migrate
```

## Step 10: Create Superuser
```bash
python manage.py createsuperuser
```

Or use the one-time promotion URL after deployment.

## Step 11: Configure Web App
1. Go to **Web** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"** (not Django wizard)
4. Select **Python 3.11**

## Step 12: Configure WSGI File
1. In the **Web** tab, click on the WSGI configuration file link
2. **Delete all content** and replace with:

```python
import os
import sys
from pathlib import Path

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/LoveConnect'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'Dating_Website.settings'

# Load environment variables from .env file
env_file = Path(path) / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key, value)

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Replace `YOUR_USERNAME`** with your PythonAnywhere username.

## Step 13: Configure Virtual Environment
1. In the **Web** tab, scroll to **"Virtualenv"** section
2. Enter the path to your virtual environment:
   - If using `mkvirtualenv`: `/home/YOUR_USERNAME/.virtualenvs/datingapp`
   - If using `venv`: `/home/YOUR_USERNAME/LoveConnect/venv`

## Step 14: Configure Static Files
1. In the **Web** tab, scroll to **"Static files"** section
2. Add a new static file mapping:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/LoveConnect/staticfiles`

## Step 15: Reload Web App
1. Scroll to the top of the **Web** tab
2. Click the big green **"Reload YOUR_USERNAME.pythonanywhere.com"** button

## Step 16: Test Your Site
Visit: `https://YOUR_USERNAME.pythonanywhere.com`

## Step 17: Create Admin User (if needed)
Visit: `https://YOUR_USERNAME.pythonanywhere.com/user/promote-me-to-admin/`
- Register a new account first
- Then access this URL to become admin

## Troubleshooting

### Error: "DisallowedHost"
- Check that your username is correct in `.env` file
- Verify `PYTHONANYWHERE_DOMAIN` matches your actual domain

### Error: "No module named 'Dating_Website'"
- Check WSGI file has correct path
- Verify `sys.path.insert(0, path)` is before Django imports

### Static Files Not Loading
- Run `python manage.py collectstatic` again
- Check static files mapping in Web tab
- Verify path is `/home/YOUR_USERNAME/LoveConnect/staticfiles`

### Database Errors
- Run migrations: `python manage.py migrate`
- PythonAnywhere uses SQLite by default (no PostgreSQL on free tier)

### Profile Pictures Not Uploading
- Free tier PythonAnywhere doesn't support uploaded files persistence
- Cloudinary is configured and will work for media storage
- Verify Cloudinary environment variables are set in `.env`

### View Error Logs
1. Go to **Web** tab
2. Click on **Error log** link
3. Check the most recent errors

## Updating Your Site

After making code changes:

1. SSH into PythonAnywhere or open Bash console
2. Navigate to project:
   ```bash
   cd ~/LoveConnect
   ```
3. Pull latest changes:
   ```bash
   git pull origin master
   ```
4. Install any new dependencies:
   ```bash
   source venv/bin/activate  # or workon datingapp
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```
7. Reload web app in **Web** tab

## Limitations of Free Tier

- **No HTTPS for custom domains** (only YOUR_USERNAME.pythonanywhere.com)
- **SQLite database only** (no PostgreSQL/MySQL)
- **CPU time limits** (100 seconds/day)
- **No scheduled tasks**
- **Files reset every 3 months** (use Cloudinary for media)

## Files Overview

```
/home/YOUR_USERNAME/LoveConnect/
├── Dating_Website/
│   ├── settings.py        # Django settings
│   ├── wsgi.py           # WSGI application
│   └── urls.py
├── user/                  # User app
├── main/                  # Main app
├── staticfiles/           # Collected static files
├── .env                   # Environment variables (create this)
├── manage.py
└── requirements.txt
```

## Environment Variables Summary

Add to `.env` file:
```
SECRET_KEY=#2lth^f$hu&bld7x76ihltzx=c)q%a2qenc^5q+6pgat&&xg61
DEBUG=False
PYTHONANYWHERE_DOMAIN=YOUR_USERNAME.pythonanywhere.com
CLOUDINARY_CLOUD_NAME=dmdjz28ru
CLOUDINARY_API_KEY=482843432266249
CLOUDINARY_API_SECRET=72h8xldIO8hDwDgopJ9M_67CzxI
```

Your site will be live at: `https://YOUR_USERNAME.pythonanywhere.com` 🚀
