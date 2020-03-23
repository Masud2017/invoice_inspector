from django.db import models

class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    company = models.TextField()
    color = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()

'''
class profileDetail(models.Model):
        email = models.ForeignKey(User, on_delete=models.CASCADE)
        color = models.TextField()

'''