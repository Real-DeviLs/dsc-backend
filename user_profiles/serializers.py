from rest_framework import serializers
from .models import UserName

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = ['username', 'url', 'platform_name']