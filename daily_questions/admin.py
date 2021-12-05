from django.contrib import admin
from .models import (Track,Leaderboard,
    Questions,Daily_Question)
# Register your models here.


class QuestionAdmin(admin.StackedInline):
    model=Questions

class Daily_QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin,]
    class Meta:
        model = Daily_Question

admin.site.register(Track)
admin.site.register(Leaderboard)
admin.site.register(Questions)
admin.site.register(Daily_Question,Daily_QuestionAdmin)
# admin.site.register(Platform)
