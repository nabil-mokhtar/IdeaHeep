from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
        user    = models.OneToOneField( User,on_delete=models.CASCADE )
        phone=models.IntegerField(null=True,blank=True,unique=True)
        photo=models.ImageField(null=True,blank=True)
        education= models.TextField(null=True,blank=True)
        job=models.TextField(null=True,max_length=30)
        country=models.CharField(max_length=20)
        cv= models.FileField()
        interstest= models.CharField(max_length=100)
        

        def __str__(self):
                return  str(self.user.username)     


