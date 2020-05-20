### Django project create  
`git checkout --orphan Server`  
`git rm -fr .`  
`rm -fr dist`  
`rm -fr node_modules`  
`wget https://raw.githubusercontent.com/jpadilla/django-project-template/master/.gitignore`  
  
`python3.8 -m venv env`  
`source env/bin/activate` #this is for Linux (MAC?)  
`pip install django`  
`pip install psycopg2` #posgresql connector  
`pip freeze >requirements.txt`  
  
`django-admin startproject app`  
`cd app`  
change file app/settings.py: 
```  
'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'gd_db',  
        'USER': '',  
        'PASSWORD': '',  
        'HOST': ''  
}  
```  
`python manage.py migrate`  
`python manage.py createsuperuser`  
`python manage.py runserver`  
  

### Django project run
`git checkout Server`  
`git pull`  
`python3.8 -m venv env`  
`source env/bin/activate` #this is for Linux (MAC?)  
`pip install -r requirements.txt`  
`cd app`  
`python manage.py runserver`  

http://127.0.0.1:8000/  
  
