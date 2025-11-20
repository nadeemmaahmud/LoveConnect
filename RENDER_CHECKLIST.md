# Render Deployment Checklist

## ✅ Pre-Deployment Checklist

- [x] Updated `requirements.txt` with production dependencies
  - dj-database-url
  - psycopg2-binary
  - whitenoise
  - gunicorn

- [x] Created `build.sh` script for Render
  - Install dependencies
  - Collect static files
  - Run migrations

- [x] Updated `settings.py` for production
  - Environment variable for SECRET_KEY
  - Environment variable for DEBUG
  - Environment variable for ALLOWED_HOSTS
  - PostgreSQL database configuration
  - WhiteNoise middleware for static files
  - Static files configuration

- [x] Created `render.yaml` configuration file

- [x] Updated `.gitignore`
  - Ignore staticfiles/
  - Ignore .env files
  - Ignore local database

- [x] Created `.env.example` template

- [x] Created `DEPLOYMENT.md` guide

- [x] Made `build.sh` executable

- [x] Tested static files collection locally

## 📋 Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Configure for Render deployment"
git push origin master
```

### 2. Create PostgreSQL Database
- Login to Render
- New → PostgreSQL
- Name: dating-website-db
- Copy Internal Database URL

### 3. Create Web Service
- New → Web Service
- Connect GitHub repo
- Configure settings:
  - Build Command: `./build.sh`
  - Start Command: `gunicorn Dating_Website.wsgi:application`

### 4. Set Environment Variables
```
SECRET_KEY=<generate-new-key>
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
DATABASE_URL=<postgres-url-from-step-2>
PYTHON_VERSION=3.12.3
```

### 5. Deploy & Create Superuser
- Deploy the application
- Open Shell in Render
- Run: `python manage.py createsuperuser`

## 🎯 Post-Deployment

- [ ] Test website loads
- [ ] Test user registration
- [ ] Test user login
- [ ] Test profile editing
- [ ] Test password change
- [ ] Test admin login
- [ ] Test admin dashboard
- [ ] Test admin edit user
- [ ] Test profile picture upload
- [ ] Verify static files load correctly

## 🔧 Optional Enhancements

- [ ] Set up custom domain
- [ ] Configure Cloudinary for media files
- [ ] Set up email backend (for password reset)
- [ ] Add SSL certificate (automatic on Render)
- [ ] Configure monitoring/alerts
- [ ] Set up database backups

## 📊 Current Configuration

- **Python Version**: 3.12.3
- **Django Version**: 5.2.8
- **Database**: PostgreSQL (Production) / SQLite (Local)
- **Static Files**: WhiteNoise
- **WSGI Server**: Gunicorn
- **Platform**: Render

## 🆘 If Something Goes Wrong

1. **Check Render Logs**
   - Dashboard → Your Service → Logs

2. **Common Issues**:
   - Build fails: Check `requirements.txt` and `build.sh`
   - Static files missing: Run `collectstatic` in shell
   - Database errors: Verify DATABASE_URL
   - Import errors: Check all dependencies installed

3. **Debug Mode** (Temporarily):
   - Set DEBUG=True in environment variables
   - Check detailed error pages
   - **Remember to set back to False!**

## 📞 Resources

- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/
- Project DEPLOYMENT.md: See detailed guide

---

**Note**: Free tier services spin down after 15 minutes of inactivity. First request may be slow.
