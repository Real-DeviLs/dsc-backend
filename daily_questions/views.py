from .models import (Daily_Question,Questions,Leaderboard,Track)
from .serializers import QuestionsSerializer,LeaderboardSerializer, TrackSerializer
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from user_profiles.models import UserProfile,UserName
from .Utils.gfg.script import fetchResponse as gfg
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .Utils import codeforces
from rest_framework import viewsets



class DailyQuestionsView(viewsets.ModelViewSet):

    """ Get track wise daily Questions for the present day """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
 

class LeaderboardView(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
 
    def perform_create(self, serializer):
        ''' generate Leaderboard from cronjob call '''
    
        questions = Questions.objects.filter(daily_question__date = timezone.now().today())
        users = UserProfile.objects.all()        
        try:
            for user in users:
                leaderboard = Leaderboard.objects.filter(user=user.user).first()
                if leaderboard is None:
                    leaderboard = Leaderboard(user=user.user)
                    leaderboard.save()
                user_platforms = UserName.objects.filter(user=user)
                user_names = {}
                for platform in user_platforms:
                    user_names[platform.platform_name]=platform.username
                
                if user_names.get('gfg') is not None:
                    gfgset,weekly_score = gfg(user_names.get('gfg')) 
                    leaderboard.weekly_score = weekly_score

                for question in questions:
                    if(question.platform =='gfg') and question.url in gfgset:
                        leaderboard.questions.add(question) 
                        leaderboard.score += question.points

                    if question.platform == 'ltc':
                        pass

                    if question.platform == 'cf':
                        if user_names.get('cf') is not None and question not in leaderboard.questions.all() and codeforces.checkCodechefSubmission(user_names.get('cf'),question.url):
                            leaderboard.questions.add(question) 
                            leaderboard.score += question.points

                leaderboard.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=e)

