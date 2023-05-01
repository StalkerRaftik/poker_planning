from django.urls import path, include
from rest_framework import routers
from game.api.game import GameViewSet
from game.api.voting import VoteViewSet
from game.api.user_temporary import TemporaryUserView
from game.api.deck import DeckViewSet, DeckCardViewSet

router = routers.DefaultRouter()
router.register(r'game', GameViewSet)
router.register(r'vote', VoteViewSet)
router.register(r'deck', DeckViewSet, basename='deck')
router.register(r'deck_card', DeckCardViewSet, basename='deck_card')

urlpatterns = [
    path('', include(router.urls)),
    path('user_temporary', TemporaryUserView.as_view())
]
