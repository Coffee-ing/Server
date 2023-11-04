from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 
                  'place', 
                  'date', 
                  'num_people', 
                  'closing_date', 
                  'tag',
                  'content']

class ListSerializer(PostSerializer): # PostSerializer 상속
    class Meta(PostSerializer.Meta):
        fields = ['title',
                  'tag',
                  'place',
                  'date',
                  'writer']