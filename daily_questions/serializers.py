from rest_framework import serializers
from rest_framework.settings import reload_api_settings
from .models import Daily_Question, Leaderboard,Questions,Track
from django.utils import timezone


class TodaysQuestionsSerializer(serializers.ListSerializer):
    
    def to_representation(self, data):
        data = data.filter(daily_question__date = timezone.now().today() )
        return super(TodaysQuestionsSerializer,self).to_representation(data)

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        list_serializer_class = TodaysQuestionsSerializer
        fields ="__all__"
    


class TrackSerializer(serializers.ModelSerializer):

    # questions = serializers.PrimaryKeyRelatedField( queryset= Questions.objects.all() , many=True)
    questions = QuestionsSerializer(many=True,read_only=True)
    class Meta:
        model = Track
        fields = ("title","description","questions")


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Leaderboard
        fields = '__all__'