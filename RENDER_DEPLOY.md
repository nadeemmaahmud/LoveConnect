# Render Deployment Guide

## One-Click Deploy to Render

### Option 1: Dashboard Setup (Recommended)

1. **Go to Render:** https://render.com/
2. **Sign in** with GitHub
3. **Click "New +" → "Web Service"**
4. **Connect Repository:** `nadeemmaahmud/LoveConnect`
5. **Configure:**
   - **Name:** `loveconnect` (or your choice)
   - **Region:** Choose closest to you
   - **Branch:** `master`
   - **Runtime:** `Python 3`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn Dating_Website.wsgi:application`
   - **Instance Type:** `Free`

6. **Add Environment Variables** (click "Advanced"):
   ```
   SECRET_KEY=#2lth^f$hu&bld7x76ihltzx=c)q%a2qenc^5q+6pgat&&xg61
   DEBUG=False
   PYTHON_VERSION=3.11.9
   CLOUDINARY_CLOUD_NAME=dmdjz28ru
   CLOUDINARY_API_KEY=482843432266249
   CLOUDINARY_API_SECRET=72h8xldIO8hDwDgopJ9M_67CzxI
   ```

7. **Add PostgreSQL Database:**
   - Click "New +" → "PostgreSQL"
   - Name it (e.g., `loveconnect-db`)
   - Select **Free tier**
   - After creation, Render auto-adds `DATABASE_URL` to your web service

8. **Deploy!** Render will automatically build and deploy

### Your Site
After deployment completes, your site will be at:
`https://loveconnect.onrender.com` (or your chosen name)

### Create Admin User
Visit: `https://loveconnect.onrender.com/user/promote-me-to-admin/`
- Register an account first
- Access this URL to become admin (works once)

## Configuration Files

### `build.sh` (Build Script)
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### Environment Variables Summary
| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `#2lth^f$hu&bld7x76ihltzx=c)q%a2qenc^5q+6pgat&&xg61` |
| `DEBUG` | `False` |
| `PYTHON_VERSION` | `3.11.9` |
| `DATABASE_URL` | Auto-set by Render PostgreSQL |
| `RENDER_EXTERNAL_HOSTNAME` | Auto-set by Render |
| `CLOUDINARY_CLOUD_NAME` | `dmdjz28ru` |
| `CLOUDINARY_API_KEY` | `482843432266249` |
| `CLOUDINARY_API_SECRET` | `72h8xldIO8hDwDgopJ9M_67CzxI` |

## What Happens on Deploy

1. Render detects Python project
2. Runs `build.sh`:
   - Installs dependencies from `requirements.txt`
   - Collects static files
   - Runs database migrations
3. Starts Gunicorn server
4. Your app is live!

## Troubleshooting

### Build Fails
- Check **Logs** tab in Render dashboard
- Verify `build.sh` is executable (should be after git push)
- Ensure all dependencies are in `requirements.txt`

### Database Errors
- Verify PostgreSQL database is created
- Check that `DATABASE_URL` appears in Environment Variables
- Render auto-links database to web service

### Static Files Not Loading
- Check build logs for collectstatic errors
- Verify WhiteNoise is in `MIDDLEWARE` (already configured)

### CSRF Errors
- Render auto-sets `RENDER_EXTERNAL_HOSTNAME`
- Settings already configured to use it for `ALLOWED_HOSTS`

### Profile Pictures Not Uploading
- Cloudinary must be configured (environment variables)
- Render's filesystem is ephemeral - Cloudinary is required for media

## Free Tier Limits

- **Web Services:** Spin down after 15 min of inactivity (first request may be slow)
- **PostgreSQL:** 1GB storage, expires after 90 days
- **Bandwidth:** 100GB/month
- **Build Minutes:** 500 minutes/month

## Updating Your Site

Render auto-deploys when you push to `master`:

```bash
git add .
git commit -m "Your changes"
git push origin master
```

Render detects the push and rebuilds automatically.

## Manual Redeploy

If you need to redeploy without code changes:
1. Go to Render dashboard
2. Click your web service
3. Click "Manual Deploy" → "Deploy latest commit"

---

**Your dating website is ready to deploy on Render!** 🚀

Just follow the dashboard setup steps above and you'll be live in minutes.
