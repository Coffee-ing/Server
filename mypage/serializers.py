from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from main.models import *
from main.serializers import *

class MyClubSerializer(ModelSerializer):
    club_id = serializers.CharField(source='club.id', read_only=True)
    club = ClubSerializer()

    class Meta:
        model = MyClub
        fields = ['club_id', 'club']


class MyLikeSerializer(ModelSerializer):
    club = ClubSerializer()

    class Meta:
        model = MyLike
        fields = ['club']
