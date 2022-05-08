from django.urls import path
from . import  views

urlpatterns = [
    path("", views.index, name='index'),
    path("test/", views.test, name='test'),
    path("<int:id>/", views.with_id, name='with_id'),
]
