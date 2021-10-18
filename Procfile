web: gunicorn app.wsgi:application --log-file - --log-level debug
heroku config:set DISABLE_COLLECTSTATIC=1
manage.py migrate