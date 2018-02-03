# CamNav


## Development

### Good tuto
https://tutorial.djangogirls.org/en/django_start_project/

### Create the project

```django-admin startproject mycamnavsite```


### Create apps

cd mymycamnavsite

```django-admin startapp main_app```

### Run the website

```python manage.py runserver```


In your browser Go to http://127.0.0.1:8000/ to see the result

### Database

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py createsuperuser```

### Sqlite3

Open database

```sqlite3 db.sqlite3```

```> .tables``` : list of tables

```> .quit```


### Create templates


### Heroku

```
heroku login

heroku apps:create navy-cm

git push heroku master
```



### AB Collection
lulu.tngnt.co


telerik chart
to draw graphs


python manage.py shell

>>> from django.contrib.auth.models import User


john - default
default = pbkdf2_sha256$24000$HsPy6t036HhT$1szz6DqaLiSXL13/p5aK7cgdA8u6zgwf+rgWOHznuoU=

User.objects.create_user('John', 'ptchankue@gmail.com','default')


insert into auth_user (username, email, password, is_superuser, first_name, last_name, is_staff,
is_active, date_joined)
values ('John-imported','ptchankue@gmail.com',
'pbkdf2_sha256$24000$HsPy6t036HhT$1szz6DqaLiSXL13/p5aK7cgdA8u6zgwf+rgWOHznuoU=',0, 'John', '', 0,
1, '2017-01-01');

>>> from django.contrib.auth import authenticate
>>> u = authenticate(username='John-imported',password='default')
>>> u


user : patricktchankue - mystery
## MySQL

mysql.server start



mysql -u root

mysql> show databases;

mysql> created database mydb;



## Django-table2

Person.objects.bulk_create([Person(name='Dieter'), Person(name='Bradley')])


brew link gettext --force


django-admin.py makemessages -l fr

manage.py compilemessages


django-autotranslate

'autotranslate' in INSTALLED_APPS

python

django-admin.py makemessages -l fr_FR -e html

## Requirements

26 Jan 2018

Actualite
Carnet du CEMM
    > deplacements
    > audiences
Carrieres
    > recrutements
Magazines
    > journaux
Marine nationale
    > organisation
    > missions
    > enjeux
    > histoire
Textes officiels
    > decrets
    > arretes
A propos
