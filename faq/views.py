from .models import Faq
from .serializers import FaqSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class FaqView(APIView):
    """
        List of All FAQ available with answers
    """
    def get(self, request, *args, **kwargs):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs,many=True)

        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):

    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)