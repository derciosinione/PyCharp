from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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


class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField()
    picture = models.ImageField(null=True, upload_to='PostImg')
    dateCreated = models.DateTimeField(default=timezone.now)
    dateUpdated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-dateCreated']

    def __str__(self):
        return f'{self.title} - {self.user.username}'

