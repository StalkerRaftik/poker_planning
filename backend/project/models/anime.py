from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

# class Anime(models.Model):
#     class AnimeStatus(models.TextChoices):
#         ANNOUNCED = 'AN', 'Анонсировано'
#         ONGOING = 'ON', 'Онгоинг'
#         RELEASED = 'RE', 'Завершено'
#
#     name = models.CharField(max_length=60, blank=True, verbose_name='Название на русском')
#     original_name = models.CharField(max_length=255, verbose_name='Оригинальное название')
#     description = models.TextField(blank=True, verbose_name='Описание')
#     premiere_date = models.DateField(blank=True, verbose_name='Дата премьеры')
#     status = models.CharField(
#         max_length=2,
#         choices=AnimeStatus.choices,
#         default=AnimeStatus.ANNOUNCED,
#         verbose_name='Статус'
#     )
#     episodes_count = models.IntegerField(default=-1, verbose_name='Всего эпизодов(-1 - неизвестно)')
#     added_episodes = models.IntegerField(default=0, verbose_name='Количество выпущенных эпизодов')
#     image = models.ImageField(upload_to='media/anime/images', verbose_name='Изображение(240x400)')
#     genres = models.ManyToManyField(Genre, related_name='anime', verbose_name='Жанры')
#     rating_calc = models.IntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(5)],
#         default=0,
#         verbose_name='Калькуляция рейтинга'
#     )
#
#     # temporary rating from dataset. Will be overwritten after ?? reviews
#     raw_rating = models.FloatField(
#         validators=[MinValueValidator(0), MaxValueValidator(10)],
#         blank=True,
#         verbose_name='Дефолтный рейтинг'
#     )
#     # temporary visits from dataset. Will be overwritten after ?? detail page visits
#     raw_visits = models.PositiveBigIntegerField(
#         blank=True,
#         verbose_name='Дефолтное количетсво посещений'
#     )
#
#     class Meta:
#         constraints = [UniqueConstraint(fields=['original_name'], name='unique_anime_original_name')]
#         verbose_name = verbose_name_plural = 'Аниме'
#
#     def __str__(self):
#         return self.name or self.original_name
