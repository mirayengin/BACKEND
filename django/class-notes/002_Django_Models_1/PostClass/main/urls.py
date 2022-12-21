"""main URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from fscohort.views import postclass,postclass1
# from dscohort.views import preclass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postclass/', include('fscohort.urls')),
    path('preclass/', include('dscohort.urls')),
    # path('postclass/', postclass),
    # path('postclass1/', postclass1),
    #? Adresleri uç uca ekleyebiliyoruz.Önce postclass a gittik ve sonra preclass yzıp gittik yada sarı kısmı direk yazarsak gideriz preclass a
    # path('postclass/preclass/', preclass),
]