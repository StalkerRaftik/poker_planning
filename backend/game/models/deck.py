from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class DeckCard(models.Model):
    value = models.CharField(max_length=16, verbose_name='Значение')
    deck = models.ForeignKey('game.Deck', on_delete=models.CASCADE, related_name='cards')

    class Meta:
        verbose_name = verbose_name_plural = 'Карта колоды'


class Deck(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Создатель', null=True)
    is_global_deck = models.BooleanField(default=False)

    class Meta:
        verbose_name = verbose_name_plural = 'Колода'
