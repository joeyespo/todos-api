release: python manage.py migrate
web: gunicorn --error-logfile=- todos.wsgi -b 0.0.0.0:$PORT
