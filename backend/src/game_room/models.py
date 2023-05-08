import uuid

from django.db import models

from user.models import User


class GameRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100, null=True)

    players = models.ManyToManyField(User)


class GameRoomUser(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    game_room = models.ForeignKey(GameRoom, null=False, on_delete=models.CASCADE)

    total_points = models.IntegerField(null=False, default=0)


