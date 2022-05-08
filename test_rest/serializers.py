from rest_framework import serializers
from .models import Person

class SerializerPerson(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age']
