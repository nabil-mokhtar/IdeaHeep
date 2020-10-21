from django.db import models
from User.models import User

# Create your models here.

class contribution(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    typeofcontrip= models.CharField(max_length=100)

    

