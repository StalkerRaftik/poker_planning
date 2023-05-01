import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'recalculate-anime-rating': {
    #     'task': 'codraw.tasks.UpdateAnimeRating',
    #     'schedule': crontab(),
    # },
}