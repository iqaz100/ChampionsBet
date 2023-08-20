from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from game_room.invitations import INVITATION_STATUSES, INVITATION_STATUSES_ENUM
from game_room.models import GameRoom, GameRoomUser, Invitation
from game_room.serializers import GameRoomSerializer, GameRoomUserSerializer, InvitationSerializer


class GameRoomView(viewsets.ModelViewSet):
    queryset = GameRoom.objects.all()
    serializer_class = GameRoomSerializer


class GameRoomUserView(viewsets.ModelViewSet):
    queryset = GameRoomUser.objects.all()
    serializer_class = GameRoomUserSerializer


class InvitationView(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    @action(methods=["post"], detail=True, url_path="accept_invitation")
    def accept_invitation(self, request, pk):
        try:
            invitation = Invitation.objects.get(id=pk)
            if invitation.invited_user != request.user:
                return Response({'error': "Brak uprawnień do wykonania tej akcji!"}, status=status.HTTP_403_FORBIDDEN)

            with transaction.atomic():
                # TODO: Do przemyslenia czy nie przenieść modelu zaproszenia
                invitation.status = INVITATION_STATUSES_ENUM.accepted.value
                invitation.save()

                GameRoomUser.objects.create(user=request.user, game_room=invitation.game_room)

            return Response({"success": "Zaproszenie zostało zaakceptowane."}, status=status.HTTP_202_ACCEPTED)

        except Invitation.DoesNotExist:
            return Response({"error": "Zaproszenie o podanym identyfikatorze nie istnieje."},
                            status=status.HTTP_404_NOT_FOUND)

