from django.db import models

# Create your models here.

team_level = (("Team Lead","Team Lead"),
              ("Senior Tech team","Senior Tech team"),
              ("Junior Tech team","Junior Tech team")
              )

class Team(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    image = models.ImageField(upload_to='team/')
    github = models.URLField()
    linkedin = models.URLField()
    email = models.EmailField()
    level = models.CharField(choices=team_level, max_length=128)

    def __str__(self):
        return self.name
         

class Partner(models.Model):
    image = models.ImageField(upload_to='partner/')
    name = models.CharField(max_length=150)
    url = models.URLField()

    def __str__(self):
        return self.name