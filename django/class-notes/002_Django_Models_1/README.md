Topics to be Covered:

Django Intro Recap

    Create virtual environment and activate
    Install Django
    Django-admin startproject
    Python manage.py startapp
    Make URL config of django project and apps

What is Django Model

    Model - View - template
    What is models
    What is ORM
    Inheriting from model class
    Model creation and what is the equivalent in database
    Brief info about field types and field options
    Create and explain str method for tables
    Pyhton manage.py makemigrations
    Pyhton manage.py migrate

View tables in Admin Site -Register tables in admin.py

    Create super user
    Login admin site
    View tables and add objects


    python -m venv env
   13  .active
   17  source env/Scripts/Activate
   18  pip freeze
   19  pip install django
   22  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
   23  python -m pip install --upgrade pip
   24  pip freeze
   25  django-admin startproject main
   26  django-admin startproject main .
   27  python manage.py runserver
   28  python manage.py runserver

   ORM-> python ile yazılan sorgu kodlarını arka plandaki database için SQL formatına çevirir.


MODELS İÇİN

   1.python manage.py createsuperuser
2.username belirleyin
3.emaili bos gecebilirsiniz.
4.password yazsaniz da gorunmuyor ama yazabiliyorsunuz, bir sifre belirleyin, tekrar sordugunda ayni sifreyi bir daha yazin
5.python manage.py runserver ile tekrar baslatin
6.url'nin sonuna admin yazarak login sayfasina gecin
7.user ve password bilginizle giris yapin