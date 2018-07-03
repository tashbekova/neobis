# neobis
## Django Project Template
The clean, fast and right way to start a new Django 2.1 powered website.
## Getting Started
Setup project environment with virtualenv and pip

<$ virtualenv project myvenv>
'''$ source project myvenv/bin/activate'''
'''$ pip install -r https://github.com/tashbekova/neobis/blob/master/django2/requirements.txt'''

## You may want to change the name `projectname`.
'''$ django-admin startproject --template https://github.com/tashbekova/neobis/tree/master/django2 projectname'''

'''$ cd projectname/'''
'''$ python manage.py migrate'''
'''$ python manage.py runserver'''
