# DjangoRestDemo

# Clone Repo
git clone https://github.com/kinjal1993/DjangoRestDemo.git

# Install virtual envrinment wrapper
pip3 install virtualenvwrapper

# Create a virtual environment for your project
python3 -m venv myvenv

# Activate virtual environment
source myvenv/bin/activate

# Install Django in your environment
pip3 install django

# Install Django in your environment
pip3 install djangorestframework

# Create a django project 
django-admin startproject restapis

# Migrate DB
python3 manage.py migrate

# Create an app in the project
python3 manage.py startapp apis

# Create Super User
python3 manage.py createsuperuser
