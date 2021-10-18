web: gunicorn app.wsgi:application --log-file - --log-level debug
python source/manage.py collectstatic --noinput
python source/manage.py migrate