from django.urls import path,include
from .views import TeamView,PartnerView


urlpatterns = [

    path("members",TeamView.as_view(),name="members"),
    path("partners",PartnerView.as_view(),name="partners"),
]