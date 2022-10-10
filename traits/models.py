from django.db import models
from rest_framework import serializers
class Trait(models.Model):
    id=serializers.IntegerField(read_only=True)
    name = models.CharField(max_length=20, unique=True)
    animals= models.ManyToManyField("animals.Animal", related_name="traits")