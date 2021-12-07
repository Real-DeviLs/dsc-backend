from django.contrib import admin

from .models import UserProfile, UserName
# Register your models here.



class UserNamesAdmin(admin.StackedInline):
    model = UserName

class UserProfilesAdmin(admin.ModelAdmin):

    inlines = [UserNamesAdmin,]

    class Meta:
        model = UserProfile

admin.site.register(UserProfile,UserProfilesAdmin)