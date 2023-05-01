# Generated by Django 3.2.7 on 2023-04-30 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_auto_20230429_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='deck',
            name='is_global_deck',
            field=models.BooleanField(default=False),
        ),
    ]
