from .models import Team,Partner
from .serializers import TeamSerializer,PartnerSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TeamView(APIView):
    
    """
    List of All team members with positions and roles
    """
    def get(self, request,*args, **kwargs):
        team = Team.objects.all()
        serializer = TeamSerializer(team,many=True,context={"request": request})
        return Response(serializer.data)
    
class PartnerView(APIView):

    """ List all Community partners and collaborators"""

    def get(self, request, *args, **kwargs):

        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners,many=True,context={"request": request})
        return Response(serializer.data)