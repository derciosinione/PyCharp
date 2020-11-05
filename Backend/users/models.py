from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField('default.jpg')
    

class NetworkCredential(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    social_network = models.CharField(verbose_name='Social Network',max_length=30,null=False,blank=False)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    link = models.CharField(max_length=100,null=False,blank=False)
    password = models.CharField(max_length=50)
    dateCreated = models.DateField(auto_now=True)
    
    def __str__(self):
        return '%s - %s' % (self.user.username,self.social_network) 

