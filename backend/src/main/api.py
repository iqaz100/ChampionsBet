from rest_framework import routers

from game_room.views import GameRoomView, GameRoomUserView
from match.views import MatchView, PredictedResultView
from team.views import TeamView
from user.views import UserView

router = routers.DefaultRouter()

router.register('matches', MatchView, basename='matches')
router.register('predicted-results', PredictedResultView, basename='predicted-results')
router.register('teams', TeamView, basename='teams')
router.register('game-rooms', GameRoomView, basename='game-rooms')
router.register('game-room-users', GameRoomUserView, basename='game-room-users')
router.register('users', UserView, basename='users')
