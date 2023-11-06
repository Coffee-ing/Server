from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from main.models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def get_my_club(request):
    if request.method == 'GET':
        my_post = MyClub.objects.all().order_by('-id')
        serializers = PostSerializer(my_post, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def get_my_apply(request):
    if request.method == 'GET':
        my_clubs = MyClub.objects.all().order_by('-id')
        serializer = MyClubSerializer(my_clubs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_my_like(request):
    if request.method == 'GET':
        my_like = MyLike.objects.all().order_by('-id')
        serializer = MyLikeSerializer(my_like, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@require_http_methods(["DELETE"])
def delete_my_apply(request, post_id):
    if request.method == 'DELETE':
        my_club = MyClub.objects.get(club_id=post_id)
        my_club.delete()
        return HttpResponse(status=204)
