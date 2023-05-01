from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint

from game.utils import generate_game_code


class Vote(models.Model):
    game_member = models.ForeignKey('game.GameMember', on_delete=models.CASCADE, verbose_name='Голосовавший')
    issue = models.ForeignKey('game.Issue', on_delete=models.CASCADE, related_name='votes', verbose_name='Задача')

    class Meta:
        verbose_name = verbose_name_plural = 'Голос'
        # TODO: Is user member of the game related to issue constraint
        constraints = [UniqueConstraint(
            fields=('game_member', 'issue'),
            name='one_vote_per_issue',
        )]


class Issue(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(max_length=2000, blank=True, verbose_name='Описание')
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='issues', verbose_name='Игра')

    final_card = models.ForeignKey(
        'game.DeckCard',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Финальная оценка'
    )

    class Meta:
        verbose_name = verbose_name_plural = 'Задача'


class GameMember(models.Model):
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='members', verbose_name='Игра')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = verbose_name_plural = 'Участник игры'
        constraints = [UniqueConstraint(
            fields=('game', 'user'),
            name='unique_game_user',
        )]


class Game(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Хост', null=True)
    deck = models.ForeignKey('game.Deck', on_delete=models.SET_NULL, null=True)
    game_code = models.CharField(default=generate_game_code, editable=False, max_length=18, unique=True)

    current_issue = models.OneToOneField(
        'game.Issue',
        on_delete=models.SET_NULL,
        null=True,
        related_name='active_for_game'
    )

    class Meta:
        verbose_name = verbose_name_plural = 'Игра'
