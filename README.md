pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py createsuperuser
(use this user to login, default: username=bawa, password=7800)

python3 manage.py runserver