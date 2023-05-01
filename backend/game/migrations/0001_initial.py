# Generated by Django 3.2.7 on 2023-04-29 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import game.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Колода',
                'verbose_name_plural': 'Колода',
            },
        ),
        migrations.CreateModel(
            name='DeckCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=16, verbose_name='Значение')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='game.deck')),
            ],
            options={
                'verbose_name': 'Карта колоды',
                'verbose_name_plural': 'Карта колоды',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_code', models.CharField(default=game.utils.generate_game_code, editable=False, max_length=18)),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игра',
            },
        ),
        migrations.CreateModel(
            name='GameMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game', verbose_name='Игра')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Участник игры',
                'verbose_name_plural': 'Участник игры',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='Описание')),
                ('on_vote', models.BooleanField(default=False, verbose_name='На голосовании')),
                ('final_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.deckcard')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='game.game', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задача',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.gamemember', verbose_name='Голосовавший')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.issue', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'Голос',
                'verbose_name_plural': 'Голос',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='current_issue',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active_for_game', to='game.issue'),
        ),
        migrations.AddField(
            model_name='game',
            name='deck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.deck'),
        ),
        migrations.AddField(
            model_name='game',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Хост'),
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('game_member', 'issue'), name='one_vote_per_issue'),
        ),
    ]
