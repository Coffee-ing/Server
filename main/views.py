from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from itertools import chain
import json


class PostViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            response_data = {"coffeeingList": serializer.data}
            return Response(response_data)


class ListViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    ordering = ['id'] # 디폴트는 최신순 정렬
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {"coffeeingList": serializer.data}
        return Response(response_data)


@api_view(['GET'])
def get_detail(request, post_id):
    club = get_object_or_404(Club, pk=post_id)
    serializer = ClubSerializer(club, context={'request': request})
    response_data = {"coffeeingList": serializer.data}
    Response(response_data)


@api_view(['GET'])
def search_clubs(request):
    keyword = request.GET.get('keyword', '')

    clubs = Club.objects.all().order_by('-id')

    if keyword:
        clubs = clubs.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(district__icontains=keyword) | Q(organizer__icontains=keyword))

    serializer = ClubSerializer(clubs, many=True, context={'request': request})
    response_data = {"coffeeingList": serializer.data}
    Response(response_data)


@api_view(['GET'])
def sorting_clubs(request):
    sorting = request.GET.get('sort', '')

    clubs = Club.objects.all().order_by('-id')

    if sorting == '최신순':
        clubs = clubs.order_by('-id')
    elif sorting == '인기순':
        clubs = clubs.order_by('-like')
    elif sorting == '마감임박순':
        clubs = clubs.order_by('deadline_yy', 'deadline_mm', 'deadline_dd')

    serializer = ClubSerializer(clubs, many=True, context={'request': request})
    response_data = {"coffeeingList": serializer.data}
    Response(response_data)


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
    return Response({"Number of likes": club.like, "Like it or not": club.iflike})


@api_view(['GET'])
def filter_category(request):
    tags = request.GET.getlist('tag', [])

    clubs = Club.objects.all().order_by('-id')

    original_clubs = ""
    friend_clubs = ""
    tour_clubs = ""
    worker_clubs = ""
    friend_clubs = ""
    beginner_clubs = ""
    why_clubs =""

    for tag in tags:
        # print(f"Received keyword: {tag}")
        if tag == 'original':
            original_clubs = clubs.filter(Q(tag__icontains=tag))
        if tag == 'friend':
            friend_clubs = clubs.filter(Q(tag__icontains=tag))
        if tag == 'tour':
            tour_clubs = clubs.filter(Q(tag__icontains=tag))
        if tag == 'worker':
            worker_clubs = clubs.filter(Q(tag__icontains=tag))
        if tag == 'beginner':
            beginner_clubs = clubs.filter(Q(tag__icontains=tag))
        if tag == 'why':
            why_clubs = clubs.filter(Q(tag__icontains=tag))

    if tags:
        clubs = list(chain(original_clubs, friend_clubs, tour_clubs, worker_clubs, beginner_clubs, why_clubs))

    serializer = ClubSerializer(clubs, many=True, context={'request': request})
    response_data = {"coffeeingList": serializer.data}
    Response(response_data)