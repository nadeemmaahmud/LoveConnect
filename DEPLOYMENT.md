# Deployment Guide for Render

## Prerequisites
- GitHub account
- Render account (free tier available)
- Project pushed to GitHub

## Step-by-Step Deployment

### 1. Push to GitHub
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin master
```

### 2. Create PostgreSQL Database on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "PostgreSQL"
3. Configure:
   - **Name**: `dating-website-db`
   - **Database**: `dating_website_db`
   - **User**: `dating_website_user`
   - **Region**: Choose closest to your users
   - **Plan**: Free
4. Click "Create Database"
5. Copy the **Internal Database URL** (starts with `postgres://`)

### 3. Create Web Service on Render

1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: `dating-website` (or your preferred name)
   - **Region**: Same as database
   - **Branch**: `master`
   - **Root Directory**: Leave empty
   - **Runtime**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn Dating_Website.wsgi:application`
   - **Plan**: Free

### 4. Add Environment Variables

In the "Environment" section, add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Click "Generate" or use your own secure key |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `DATABASE_URL` | Paste the Internal Database URL from step 2 |
| `PYTHON_VERSION` | `3.12.3` |

### 5. Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Install dependencies
   - Collect static files
   - Run migrations
   - Start the application

### 6. Create Superuser

After successful deployment:

1. Go to your web service dashboard
2. Click "Shell" tab
3. Run:
```bash
python manage.py createsuperuser
```
4. Follow the prompts to create your admin account

### 7. Access Your Application

- **Website**: `https://your-app-name.onrender.com`
- **Admin Panel**: `https://your-app-name.onrender.com/admin/`
- **Admin Dashboard**: `https://your-app-name.onrender.com/user/admin/dashboard/`

## Important Notes

### Free Tier Limitations
- Apps spin down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- 750 hours/month free (enough for one always-on service)

### Media Files (Profile Pictures)

The current configuration stores media files on the Render server. For production, consider:

1. **Cloudinary** (Recommended for images)
2. **AWS S3**
3. **Render Disk Storage** (Persistent disk add-on)

To add Cloudinary:
```bash
pip install django-cloudinary-storage
```

Add to `requirements.txt` and configure in `settings.py`.

### Database Backups

Render Free PostgreSQL doesn't include automated backups. Consider:
- Upgrading to paid plan for backups
- Manual backups via `pg_dump`
- Using Render's backup feature in paid tiers

### Custom Domain

1. Go to web service settings
2. Click "Custom Domain"
3. Add your domain
4. Update DNS records as instructed
5. Update `ALLOWED_HOSTS` environment variable

## Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Verify `requirements.txt` is correct
- Ensure `build.sh` is executable

### Static Files Not Loading
- Check `STATIC_ROOT` in settings
- Verify WhiteNoise is in `MIDDLEWARE`
- Run `python manage.py collectstatic` in shell

### Database Connection Issues
- Verify `DATABASE_URL` is correctly set
- Check database is in same region
- Use Internal Database URL, not External

### Application Errors
- Check application logs in Render dashboard
- Ensure `DEBUG=False` in production
- Verify all environment variables are set

## Monitoring

- **Logs**: Available in Render dashboard
- **Metrics**: CPU, Memory, Request count
- **Alerts**: Configure in Render settings

## Updates

To deploy updates:
```bash
git add .
git commit -m "Your update message"
git push origin master
```

Render will automatically detect changes and redeploy.

## Cost Optimization

Free tier includes:
- 1 PostgreSQL database (1GB)
- 1 web service (750 hours/month)
- 100GB bandwidth

To avoid charges:
- Monitor usage in dashboard
- Use free tier limits wisely
- Upgrade only when needed

## Support

- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com/)
- [Django Deployment Guide](https://docs.djangoproject.com/en/5.2/howto/deployment/)
