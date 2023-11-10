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
    serializer_class = ClubSerializer
    ordering = ['id'] # 디폴트는 최신순 정렬


@api_view(['GET'])
def get_detail(request, post_id):
    club = get_object_or_404(Club, pk=post_id)
    serializer = ClubSerializer(club)
    return Response(serializer.data)


@api_view(['GET'])
def search_clubs(request):
    data = json.loads(request.body)
    keyword = data.get('keyword')

    clubs = Club.objects.all().order_by('-id')

    if keyword:
        clubs = clubs.filter(Q(title__icontains=keyword) | Q(district__icontains=keyword) | Q(organizer__icontains=keyword))
    else:
        pass

    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sorting_clubs(request):
    data = json.loads(request.body)
    sorting = data.get('sort')

    clubs = Club.objects.all().order_by('-id')

    if sorting == '최신순':
        clubs = clubs.order_by('-id')
    elif sorting == '인기순':
        clubs = clubs.order_by('-like')
    elif sorting == '마감임박순':
        clubs = clubs.order_by('deadline_yy', 'deadline_mm', 'deadline_dd')

    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def register_club(request, post_id):
    # if not request.user.is_authenticated:
    #     return redirect(accounts_views.home)
    club = get_object_or_404(Club, pk=post_id)
    MyClub.objects.get_or_create(club=club)
    return Response({"message": "succeed"})


@api_view(['GET', 'POST'])
def set_wishlist(request, post_id):
    club = get_object_or_404(Club, pk=post_id)
    if club.iflike:
        club.like -= 1
        club.iflike = False
        MyLike.objects.filter(club=club).delete()
    else:
        club.like += 1
        club.iflike = True
        MyLike.objects.create(club=club)
    club.save()
    return Response({"좋아요 개수": club.like, "좋아요 여부": club.iflike})
