# from celery import Task
#
# from django.db.models import Avg, OuterRef, Subquery, IntegerField
# from django.db.models.functions import Coalesce
#
# from project.celery import app
# from project.models import Anime, Rating

#
# class UpdateAnimeRating(Task):
#     @staticmethod
#     def run(*args, **kwargs):
#         avg_rating_subqs = Rating.objects \
#             .filter(anime=OuterRef('id')) \
#             .values('anime') \
#             .annotate(avg=Avg('value')) \
#             .order_by() \
#             .values('avg')
#         Anime.objects.update(rating_calc=Coalesce(Subquery(avg_rating_subqs), 0, output_field=IntegerField()))
#
#
# UpdateAnimeRatingTask = app.register_task(UpdateAnimeRating())
