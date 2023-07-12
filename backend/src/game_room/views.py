from django.shortcuts import render
from rest_framework import viewsets

from game_room.models import GameRoom, GameRoomUser
from game_room.serializers import GameRoomSerializer, GameRoomUserSerializer


class GameRoomView(viewsets.ModelViewSet):
    queryset = GameRoom.objects.all()
    serializer_class = GameRoomSerializer


class GameRoomUserView(viewsets.ModelViewSet):
    queryset = GameRoomUser.objects.all()
    serializer_class = GameRoomUserSerializer

