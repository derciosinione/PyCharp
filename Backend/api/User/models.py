from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField('default.jpg')
    

