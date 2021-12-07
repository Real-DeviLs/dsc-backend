from django.shortcuts import render
from .models import UserName,UserProfile
from rest_framework import viewsets
from .serializers import UserNameSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserNameSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        profile = UserProfile.objects.filter(user=user).first()
        return UserName.objects.filter(user=profile)

    def perform_create(self, serializer):
        user = self.request.user
        profile = UserProfile.objects.filter(user=user).first()
        serializer.save(user=profile)