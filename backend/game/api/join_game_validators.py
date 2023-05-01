from django.contrib.auth.models import User
from rest_framework import serializers

from game.models import Game, Issue, GameMember, Deck, DeckCard
from game.models.game import Vote


class JoinGameSerializer(serializers.ModelSerializer):
    game_code = serializers.CharField()

    class Meta:
        model = Game
        fields = ('game_code',)


class InfoCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckCard
        fields = ('id', 'value',)


class InfoDeckSerializer(serializers.ModelSerializer):
    cards = InfoCardsSerializer(many=True)

    class Meta:
        model = Deck
        fields = ('id', 'name', 'cards')


# TODO: Change direct user model import to get method across all project
class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class InfoGameMembersSerializer(serializers.ModelSerializer):
    user = InfoUserSerializer(allow_null=True)

    class Meta:
        model = GameMember
        fields = ('id', 'user')


class InfoVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'game_member')


class InfoIssuesSerializer(serializers.ModelSerializer):
    votes = InfoVotesSerializer(many=True)

    class Meta:
        model = Issue
        fields = ('id', 'name', 'description', 'final_card', 'votes')


class GameInfoSerializer(serializers.ModelSerializer):
    deck = InfoDeckSerializer()
    members = InfoGameMembersSerializer(many=True)
    issues = InfoIssuesSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id', 'host', 'game_code', 'current_issue', 'deck', 'members', 'issues')
