from rest_framework import serializers

from .models import Faq



class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"

    def create(self,validated_data):

        faq = Faq(**validated_data)
        faq.save()

        return faq