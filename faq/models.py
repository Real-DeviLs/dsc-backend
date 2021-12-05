from django.db import models

# Create your models here.


class Faq(models.Model):

    question = models.TextField()
    answer = models.TextField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):

        return self.question