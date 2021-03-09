echo 'Applying migrations...'
python3 manage.py migrate

echo 'Collecting static files...'
python3 manage.py runserver 0.0.0.0:8000