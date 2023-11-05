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
def get_my_clubs(request):
    if request.method == 'GET':
        my_clubs = MyClub.objects.all().order_by('-id')
        serializer = MyClubSerializer(my_clubs, many=True)
        return Response(serializer.data)