from django.contrib import admin

from .models import UserDetails, UserNames
# Register your models here.



class UserNamesAdmin(admin.StackedInline):
    model = UserNames

class UserDetailsAdmin(admin.ModelAdmin):

    inlines = [UserNamesAdmin,]

    class Meta:
        model = UserDetails

admin.site.register(UserDetails,UserDetailsAdmin)