from django.db import models
from User.models import  Users

# Create your models here.
class Team (models.Model):
    name= models.CharField(max_length=100)
    user= models.ManyToManyField(Users)

     