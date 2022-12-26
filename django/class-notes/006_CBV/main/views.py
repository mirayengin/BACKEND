from django.http import HttpResponse

def real_home(request):
    return HttpResponse('This main home page......')
















    


#?kurmak için sırasıyla;
#?python -m venv env
#!source env/Scripts/Activate (windows-bash için)
#?pip install -r requirements.txt
#?python manage.py createsuperuser
#!python manage.py runserver