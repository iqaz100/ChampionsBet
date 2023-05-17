from rest_framework import serializers

from match.models import Match, PredictedResult


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            'id',
            'game_room',
            'home_team',
            'away_team',
            'result',
        )


class PredictedResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictedResult
        fields = (
            'id',
            'match',
            'user',
            'home_team_score',
            'away_team_score',
        )
