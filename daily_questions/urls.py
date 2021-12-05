from django.urls import path,include
from .views import Daily_QuestionView,LeaderboardView


urlpatterns = [

    path("todays_questions",Daily_QuestionView.as_view(),name="todays_questions"),
    path("leaderboard/",LeaderboardView.as_view(),name="leaderboard")
]