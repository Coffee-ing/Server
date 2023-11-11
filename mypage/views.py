from django.shortcuts import render, get_object_or_404
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
        serializer = PostSerializer(my_post, many=True, context={'request': request})
        data = {"coffeeingList": serializer.data}

        return Response(data)

@api_view(['GET'])
def get_my_apply(request):
    if request.method == 'GET':
        my_clubs = MyClub.objects.all().order_by('-id')
        serializer = MyClubSerializer(my_clubs, many=True, context={'request': request})
        data = {"coffeeingList": serializer.data}

        return Response(data)


@api_view(['GET'])
def get_my_like(request):
    if request.method == 'GET':
        my_like = MyLike.objects.all().order_by('-id')
        serializer = MyLikeSerializer(my_like, many=True, context={'request': request})
        data = {"coffeeingList": serializer.data}

        return Response(data)


@api_view(['DELETE'])
@require_http_methods(["DELETE"])
def delete_my_apply(request, post_id):
    if request.method == 'DELETE':
        my_club = get_object_or_404(MyClub, pk=post_id)
        my_club.delete()
        return HttpResponse(status=204)
