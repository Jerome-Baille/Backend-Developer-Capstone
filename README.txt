Welcome to my assignement for the course "Capstone Backend Developer"

1. To launch the project

- Pipenv shell
- Pipenv install
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

2. The different endpoints are:

# Admin and auth
admin/
auth/
api-token-auth/

# Views
home/
about/
reservations/

# API
menu/,
menu_item/<int:pk>/,  

bookings/tables/
bookings/tables/<int:pk>/


3. To test the project

# To launch all the tests, run:
python manage.py test tests/