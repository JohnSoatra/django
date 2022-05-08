from django.http import JsonResponse
from .models import Person
from .serializers import SerializerPerson
from rest_framework.decorators import api_view

Get = 'GET'
Post = 'POST'
Put = 'PUT'
Delete = 'DELETE'

@api_view([Get, Post])
def people(request):
    if (request.method == Get):
        people = Person.objects.all()
        serializer = SerializerPerson(instance=people, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    else:
        serializer = SerializerPerson(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)

@api_view([Get, Put, Delete])
def person(request, id):
    try:
        person = Person.objects.get(id=id)
    except:
        return JsonResponse(data={'msg': 'not found'})
    
    if request.method == Get:
        serializer = SerializerPerson(instance=person)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == Put:
        serializer = SerializerPerson(instance=person, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return JsonResponse(data={'msg': 'invalid data'})
    else:
        serializer = SerializerPerson(instance=person)
        temp = serializer.data
        person.delete()
        return JsonResponse(data=temp, safe=False)
