from rest_framework import serializers

from .models import Team,Partner


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"
        
        def get_image(self,team):
            request = self.context.get('request')
            image_url = team.image.url
            return request.build_absolute_uri(image_url)
        def create(self,validated_data):

            team = Team(**validated_data)
            team.save()

            return team


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

        def get_image(self,partner):
            print("ethe")
            print("ethe")
            print("ethe")
            print("ethe")
            request = self.context.get('request')
            image_url = partner.image.url
            return request.build_absolute_uri(image_url)


        def create(self,validated_data):
            partner = Partner(**validated_data)
            partner.save()
            return partner
