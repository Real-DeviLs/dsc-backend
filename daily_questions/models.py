from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


platform_choices = (('gfg', 'gfg'), ('cf', 'cf'), ('ltc', 'ltc'))


class Daily_Question(models.Model):
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ('-date',)

class Track(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Questions(models.Model):
    daily_question = models.ForeignKey(Daily_Question, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True)
    url = models.URLField()
    points = models.IntegerField(default=0)
    platform = models.CharField(max_length=150, choices=platform_choices)
    track = models.ForeignKey(Track, null=True, blank=True,related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Leaderboard(models.Model):

    user = models.OneToOneField(User, related_name="leaderboard", on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions, default=None, blank=True)
    weekly_score = models.IntegerField(default=0, blank=True)
    daily_score = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username
