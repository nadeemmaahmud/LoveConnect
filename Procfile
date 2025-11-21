release: python manage.py migrate --noinput
web: gunicorn Dating_Website.wsgi:application --bind 0.0.0.0:$PORT
