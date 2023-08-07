import uuid

from django.db import models

from game_room.invitations import INVITATION_STATUSES, INVITATION_STATUSES_ENUM
from user.models import User


class GameRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100, null=True)

    players = models.ManyToManyField(User)

    is_private = models.BooleanField(default=False)


class GameRoomUser(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    game_room = models.ForeignKey(GameRoom, null=False, on_delete=models.CASCADE)

    total_points = models.IntegerField(null=False, default=0)


class Invitation(models.Model):
    invited_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    inviting_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    game_room = models.ForeignKey(GameRoom, null=False, on_delete=models.CASCADE)

    status = models.CharField(choices=INVITATION_STATUSES, max_length=100,
                              default=INVITATION_STATUSES_ENUM.pending.value)


