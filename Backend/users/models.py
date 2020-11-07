from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField('default.jpg')
    

class NetworkCredential(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    social_network = models.CharField(verbose_name='Social Network',max_length=30,null=False,blank=False)
    username = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True,blank=True)
    link = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    dateCreated = models.DateField(auto_now=True)
    
    def __str__(self):
        return '%s - %s' % (self.user.username,self.social_network) 

