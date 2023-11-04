from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

class PostViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = PostSerializer

class ListViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ListSerializer

@api_view(['GET'])
def search_clubs(request):
    data = json.loads(request.body)
    keyword = data.get('keyword')
    sorting = data.get('sort')

    clubs = Club.objects.all().order_by('-id')

    if keyword == ' ':
        pass
    elif keyword: # 제목, 지역, 작성자
        clubs = clubs.filter(Q(title__icontains=keyword) | Q(district__icontains=keyword) | Q(organizer__icontains=keyword))

    if sorting == '인기순':
        clubs = clubs.order_by('-like')
    elif sorting == '마감임박순':
        clubs = clubs.order_by('deadline_yy', 'deadline_mm', 'deadline_dd')

    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_detail(request, post_id):
    club = Club.objects.get(pk=post_id)
    serializer = ClubSerializer(club)
    return Response(serializer.data)
