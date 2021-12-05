from .models import (Daily_Question,Questions,Leaderboard,Track)
from .serializers import TrackSerializer,QuestionsSerializer,LeaderboardSerializer
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from register_login.models import UserDetails,UserNames
from .Utils.gfg.script import fetchResponse as gfg

class Daily_QuestionView(APIView):

    """ Get track wise daily Questions for the present day """
    
    
    def get(self, request, *args, **kwargs):
        tracks = Track.objects.filter()
        serializer = TrackSerializer(tracks,many=True)
        return Response(serializer.data)


class LeaderboardView(APIView):

    def get(self, request, *args, **kwargs):
        ''' Get Leaderboard details '''

        leaderboard = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(leaderboard,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ''' generate Leaderboard from cronjob call '''
    
        questions = Questions.objects.filter(daily_question__date = timezone.now().today())
        users = UserDetails.objects.all()        
        

        try:

            for user in users:
                
                leaderboard = Leaderboard.objects.filter(user=user.user).first()
            
                if leaderboard is None:
                    leaderboard = Leaderboard(user=user.user)

                user_platforms = UserNames.objects.filter(user=user)
                user_names = {}
                for platform in user_platforms:
                    
                    user_names[platform.platform_name]=platform.name
                
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
                        pass

                leaderboard.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=e)




