# Railway Deployment Guide

## Project Status
✅ Code is ready for deployment
✅ Railway configuration optimized
✅ Database migrations automated
✅ Cloudinary integration configured

## Required Environment Variables

Add these to your Railway service (Settings → Variables):

```bash
# Django Configuration
SECRET_KEY=#2lth^f$hu&bld7x76ihltzx=c)q%a2qenc^5q+6pgat&&xg61
DEBUG=False

# Cloudinary (Media Storage)
CLOUDINARY_CLOUD_NAME=dmdjz28ru
CLOUDINARY_API_KEY=482843432266249
CLOUDINARY_API_SECRET=72h8xldIO8hDwDgopJ9M_67CzxI
```

**Note:** `DATABASE_URL` is automatically provided by Railway's PostgreSQL service.

## Deployment Steps

1. **Connect GitHub Repository**
   - Go to Railway dashboard
   - Create new project → Deploy from GitHub
   - Select `nadeemmaahmud/LoveConnect` repository
   - Railway will auto-deploy on every push to `master`

2. **Add PostgreSQL Database**
   - In your Railway project, click "New"
   - Select "Database" → "PostgreSQL"
   - Railway automatically links it via `DATABASE_URL`

3. **Configure Environment Variables**
   - Go to your service → Settings → Variables
   - Add each variable from the list above
   - Click "Deploy" to apply changes

4. **Generate Public Domain**
   - Go to Settings → Networking
   - Click "Generate Domain"
   - Your site will be available at `https://yourapp.up.railway.app`

5. **Create Admin User**
   - Visit: `https://yourapp.up.railway.app/user/promote-me-to-admin/`
   - Register a new account first
   - Then access the promotion URL (works only once for the first user)

## Technical Details

- **Python Version:** 3.11.9 (specified in `runtime.txt`)
- **Workers:** 3 Gunicorn workers with 2 threads each (optimized for 512MB RAM)
- **Database:** PostgreSQL (Railway Internal)
- **Media Storage:** Cloudinary
- **Static Files:** WhiteNoise

## What Happens on Deploy

1. Railway installs Python 3.11.9
2. Installs dependencies from `requirements.txt`
3. Runs release command:
   - `python manage.py migrate --noinput` (creates/updates database tables)
   - `python manage.py collectstatic --noinput` (gathers static files)
4. Starts Gunicorn web server with 3 workers

## Monitoring

- **View Logs:** Railway dashboard → Deployments → Latest → View Logs
- **Check Status:** Service should show "Active" status
- **Memory Usage:** Monitor to ensure it stays under 512MB

## Troubleshooting

### Workers Still Causing OOM
If you still see "Worker (pid:X) was sent SIGKILL! Perhaps out of memory?":
- Railway may be caching old builds
- Go to Settings → Delete Service → Recreate from GitHub

### Profile Pictures Not Showing
- Verify Cloudinary environment variables are set correctly
- Check logs for Cloudinary connection errors
- Visit `/user/debug-profile-pic/` to see Cloudinary config status

### CSRF Errors
- Domain is already whitelisted for `*.railway.app`
- If using custom domain, add it to `CSRF_TRUSTED_ORIGINS` in `settings.py`

## Repository Structure
```
DatingApp/
├── Dating_Website/     # Main Django project
│   ├── settings.py     # Production-ready settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── user/               # User authentication app
│   ├── models.py       # Custom User model
│   ├── views.py        # Auth views + admin dashboard
│   ├── forms.py        # User forms
│   └── templates/      # User templates
├── main/               # Landing page app
│   ├── views.py
│   └── templates/
├── Procfile            # Railway deployment commands
├── runtime.txt         # Python version
├── requirements.txt    # Python dependencies
└── manage.py           # Django management
```

## Next Steps After Deployment

1. Test user registration
2. Upload a profile picture to verify Cloudinary
3. Access admin dashboard at `/user/admin/dashboard/`
4. Access Django admin at `/admin/`
