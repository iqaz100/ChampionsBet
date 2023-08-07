import uuid

from django.db import models

from game_room.models import GameRoom
from team.models import Team
from user.models import User


class Match(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    game_room = models.ForeignKey(GameRoom, null=False, on_delete=models.CASCADE)

    home_team = models.ForeignKey(Team, null=False, on_delete=models.CASCADE, related_name='home_team')

    away_team = models.ForeignKey(Team, null=False, on_delete=models.CASCADE, related_name='away_team')

    home_team_score = models.IntegerField(null=False)

    away_team_score = models.IntegerField(null=False)


class PredictedResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    match = models.ForeignKey(Match, null=False, on_delete=models.CASCADE)

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    home_team_score = models.IntegerField(null=False)

    away_team_score = models.IntegerField(null=False)


