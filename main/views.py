from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer, ListSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ListSerializer