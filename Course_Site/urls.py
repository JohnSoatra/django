from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from meetups import views


def home(req):
    if req.method == 'get':
        return HttpResponse('Home page');
    else:
        return HttpResponse('Post Home page')
    


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls, name='index'),
    path('meetups/', include("meetups.urls")),
]
