from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

platform_choices = (("gfg","gfg"),("ltc","ltc"),("cf","cf"))

class UserDetails(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
    
    def __str__(self):
        return self.user.username

class UserNames(models.Model):

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    platform_name = models.CharField(max_length=50,choices=platform_choices)

    def __str__(self):
        return self.name

