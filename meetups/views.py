from django.http import HttpResponse
from django.shortcuts import render
from .models import Meetups
    
def index(req):
    meetups = Meetups.objects.all()
    return render(req, 'meetups/index.html', {
        'meetups': meetups
    })

def with_id(req, id):
    meetup = Meetups.objects.get(id=id)
    return render(req, 'meetups/with_id.html', {
        'meetup': meetup
    })
    
def changeName(obj):
    obj['name'] = "New"
    print(obj)
    return None

def test(req):
    obj = { 'name': 'Soatra' }
    return render(req, 'meetups/test.html', {
        'obj': obj,
        'fun': lambda: changeName(obj)
    })