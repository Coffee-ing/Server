from rest_framework.serializers import ModelSerializer
from .models import Club

class PostSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = ['title', 
                'district', 
                'meet_time', 
                'num_people', 
                'deadline_yy',
                'deadline_mm',
                'deadline_dd', 
                'tag',
                'content']


class ListSerializer(PostSerializer): # PostSerializer 상속
    class Meta(PostSerializer.Meta):
        fields = ['title',
                'tag',
                'district',
                'meet_time',
                'organizer']


class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
