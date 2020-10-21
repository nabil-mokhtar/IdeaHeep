from django.db import models
from User.models import Users 
from Team.models import Team
from Category.models import Categories
from Contripution.models import contribution
from Comment.models import comments

# Create your models here.
class Projects(models.Model):
    user= models.ForeignKey(Users,on_delete=models.CASCADE,blank=True)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,blank=True)
    #many to many in case more than one team can contrib in one project
    photo=models.ImageField(null=True)
    date=models.DateTimeField(auto_now=True)
    rating =models.IntegerField(null=True)
    detail=models.TextField()
    name=models.CharField(max_length=100)
    vedio=models.URLField()

    category=models.ManyToManyField(Categories)
    contributions=models.ForeignKey(contribution,on_delete=models.CASCADE, blank=True,null=True) 
    # comments= models.ForeignKey(comments,on_delete=models.CASCADE,blank=True, null=True)


    
      

