from django.shortcuts import render
from rest_framework import viewsets

from match.models import Match, PredictedResult
from match.serializers import MatchSerializer, PredictedResultSerializer


class MatchView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class PredictedResultView(viewsets.ModelViewSet):
    queryset = PredictedResult.objects.all()
    serializer_class = PredictedResultSerializer


