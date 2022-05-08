from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    def __str__(self) -> str:
        return f"{self.name} - {self.age}"
