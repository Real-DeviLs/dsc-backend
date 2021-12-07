from django.contrib import admin

from .models import UserDetail, UserName
# Register your models here.



class UserNamesAdmin(admin.StackedInline):
    model = UserName

class UserDetailsAdmin(admin.ModelAdmin):

    inlines = [UserNamesAdmin,]

    class Meta:
        model = UserDetail

admin.site.register(UserDetail,UserDetailsAdmin)