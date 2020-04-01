from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.TextField(max_length = 50, blank=True)
    company = models.TextField(max_length=50,blank=True)
    color = models.TextField(max_length=50,blank=True)
    gender = models.TextField(max_length=50,blank=True)
    profilePic = models.TextField(blank = True)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Setting(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    theme = models.TextField(max_length=15)

