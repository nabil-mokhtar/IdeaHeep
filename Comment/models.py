from django.db import models
from User.models import User

# Create your models here.


class comments(models.Model):
    content=models.TextField(max_length=1000)
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    ups=models.IntegerField(blank=True)
    downs=models.IntegerField(blank=True)
