from django.db import models
from authApp.models import *
from django.contrib.auth.models import User


# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class InvoiceInfo(models.Model):
    comp = models.TextField(max_length=50,blank = True)
    logoComp = models.TextField(blank=True)
    emailComp = models.TextField(blank=True)
    addressComp = models.TextField(blank=True)
    phoneNum = models.IntegerField(blank=True)

    user = models.OneToOneField(User,on_delete=models.CASCADE) # Joining this model/table with main model/table User from django.contrib.auth.models
   