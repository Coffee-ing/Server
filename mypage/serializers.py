from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from main.models import *
from main.serializers import *

class MyClubSerializer(ModelSerializer):
    club_id = serializers.CharField(source='club.id', read_only=True)
    title = serializers.CharField(source='club.title', read_only=True)
    district = serializers.CharField(source='club.district', read_only=True)
    meet_time = serializers.CharField(source='club.meet_time', read_only=True)
    organizer = serializers.CharField(source='club.organizer', read_only=True)

    class Meta:
        model = MyClub
        fields = ['id', 'club_id', 'title', 'district', 'meet_time', 'organizer']


class MyLikeSerializer(ModelSerializer):
    club = ClubSerializer()

    class Meta:
        model = MyLike
        fields = ['club']
