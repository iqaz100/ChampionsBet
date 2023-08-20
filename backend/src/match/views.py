from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from match.models import Match, PredictedResult
from match.serializers import MatchSerializer, PredictedResultSerializer

from backend.src.match.helpers import calculate_points


class MatchView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        if request.data.get('home_team_score', None) or request.data.get('away_team_score', None):
            match = Match.objects.get(id=instance.id)
            if match.home_team_score and match.away_team_score:
                for result in instance.results:
                    result.bet_score = calculate_points(match.home_team_score, match.away_team_score,
                                     result.home_team_score, result.away_team_score)
                    result.save()

        return Response(serializer.data)


class PredictedResultView(viewsets.ModelViewSet):
    queryset = PredictedResult.objects.all()
    serializer_class = PredictedResultSerializer


