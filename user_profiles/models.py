from django.contrib.auth.models import User
from django.db import models
# Create your models here.

platform_choices = (("gfg","gfg"),("ltc","ltc"),("cf","cf"))

class UserProfile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
    def __str__(self):
        return self.user.username

class UserName(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    url = models.URLField()
    platform_name = models.CharField(max_length=50,choices=platform_choices)

    def __str__(self):
        return self.username

