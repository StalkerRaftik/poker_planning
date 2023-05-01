from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from game.api.api_permissions import GameAdminPermission
from game.api.join_game_validators import JoinGameSerializer, GameInfoSerializer
from game.models import Game, Issue, GameMember


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('deck',)


class SetIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('current_issue',)


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (GameAdminPermission,)

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

    @action(detail=True, methods=['post'], serializer_class=SetIssueSerializer)
    def set_current_issue(self, request, *args, **kwargs):
        game = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        issue = Issue.objects.get(id=serializer.validated_data['current_issue'])

        if issue.game != game:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        game.current_issue = issue
        game.save()
        return Response(status=status.HTTP_200_OK)

    @swagger_auto_schema(
        methods=['post'],
        request_body=JoinGameSerializer,
        responses={200: GameInfoSerializer()}
    )
    @action(detail=False, methods=['post'], permission_classes=(IsAuthenticated,), serializer_class=JoinGameSerializer)
    def join_game(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game_code = serializer.validated_data['game_code']

        game = Game.objects.get(game_code=game_code)
        GameMember.objects.create(game=game, user=request.user)

        game = Game.objects\
            .filter(game_code=game_code)\
            .select_related('deck')\
            .prefetch_related('deck__cards')\
            .prefetch_related('issues__votes')\
            .prefetch_related(Prefetch(
                'members',
                queryset=GameMember.objects.select_related('user')
            ))\
            .first()

        return Response(GameInfoSerializer(game).data, status=status.HTTP_200_OK)
