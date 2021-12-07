from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import UserProfile
from daily_questions.models import Leaderboard


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Leaderboard.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)