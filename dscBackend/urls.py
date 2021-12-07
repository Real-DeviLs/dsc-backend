"""dscBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from rest_framework.routers import DefaultRouter
from user_profiles.views import UserProfileView
from daily_questions.views import DailyQuestionsView, LeaderboardView

routers=DefaultRouter()
routers.register('user-profile',UserProfileView,basename='user-profile')
routers.register('daily-questions',DailyQuestionsView,basename='daily-questions')
routers.register('leaderboard',LeaderboardView,basename='leaderboard')



urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('rest_registration.api.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="DSC Backend",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('faq/', include('faq.urls')),
    path('team/', include('team.urls')),
    path('questions/', include('daily_questions.urls')),
    path('auth', include('rest_framework.urls')),
    path('',include(routers.urls)),
]
