echo 'Applying migrations...'
python3 manage.py migrate --verbosity=0

echo 'Collecting static files...'
python3 manage.py collectstatic --noinput --verbosity=0

python3 manage.py runserver 0.0.0.0:8000