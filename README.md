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
pip install django-rest-framework

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

# Error no reconce el rest_framework
    Control+ shift + p.
    type 'Python: Select Interpreter' and select the same.
    choose your virtual env from the list if it is not listed please choose Enter Interpreter path'
    path of your virtual env python.exe file.

mine was : D:\Python\Python_Django\trydjango\env\Scripts\python.exe

You can find similar path according to your project