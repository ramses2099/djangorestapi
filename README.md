# djangorestapi
MongoDB + Django Rest Framework CRUD Rest API example

# create virtual enviroment
virtualenv env

## update pip 
python -m pip install --upgrade pip

# Install Django REST framework
# Django REST framework helps us to build RESTful Web Services flexibly.
# To install this package, run command:
pip install django
pip install djangorestframework

# Create django project
django-admin startproject [project_name] .

django-admin startproject core .

# Run development server
python manage.py runserver

# Get module requirements
pip freeze > requirements.txt

# Start App
django-admin startapp api

# Make migrations
python manage.py makemigrations

# Run migration
python manage.py migrate

