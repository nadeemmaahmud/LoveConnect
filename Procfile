release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn Dating_Website.wsgi:application --bind 0.0.0.0:$PORT
