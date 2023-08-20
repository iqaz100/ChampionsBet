from rest_framework import serializers

from game_room.models import GameRoom, GameRoomUser, Invitation


class GameRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRoom
        fields = (
            'id',
            'name',
            'players',
        )


class GameRoomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRoomUser
        fields = (
            'user',
            'game_room',
            'total_points'
        )


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = (
            'id',
            'user',
            'game_room',
            'status'
        )
