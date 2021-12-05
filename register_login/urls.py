

from django.urls import path,include
from .views import TwitterLogin,GithubLogin
urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/github/', GithubLogin.as_view(), name='github_login')
]