import csv
import traceback
from datetime import datetime
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

import requests
from django.core.files.base import File
from django.core.management.base import BaseCommand
from django.db import transaction

from codraw.models.anime import Anime, Genre

# .csv header:
# ['uid', 'title', 'synopsis', 'genre', 'aired', 'episodes',
# 'members', 'popularity', 'ranked', 'score', 'img_url', 'link']

base_path = 'media/anime/images'
genres = dict()


def get_date(raw_date):
    date_to_parse = raw_date.split('to')[0].strip().replace(',', '')
    return datetime.strptime(date_to_parse, '%b %d %Y')


def get_genre_objects(genres_list):
    genres_to_return = []
    for genre_name in genres_list:
        genre = genres.get(genre_name, None)
        if genre:
            genres_to_return.append(genre)
            continue

        genre = Genre.objects.get_or_create(name=genre_name)[0]
        genres[genre_name] = genre
        genres_to_return.append(genre)

    return genres_to_return


def get_img(url):
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        return

    path = f'{base_path}/{url.split("/")[-1]}'
    with open(path, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    return path


@transaction.atomic
def load_anime(row):
    episodes_count = int(float(row[5])) if row[5] else ''
    anime_data = {
        'original_name': row[1],
        'premiere_date': get_date(row[4]),
        'status': Anime.AnimeStatus.RELEASED,
        'added_episodes': episodes_count,
        'episodes_count': episodes_count,
        'description': row[2],
        'raw_rating': row[9],
        'raw_visits': row[6],
    }
    anime = Anime(**dict(filter(
        lambda item: bool(item[1]),
        anime_data.items()
    )))
    img_path = get_img(row[10])
    with open(img_path, 'rb') as f:
        anime.image.save(img_path, File(f), save=False)
    anime.save()

    genres_list = list(map(
        lambda genre_name: genre_name.strip(),
        row[3][1:-1].replace('\'', '').split(',')
    ))
    anime.genres.add(*get_genre_objects(genres_list))

    return anime.original_name


def worker_job(row):
    if row is None:
        return
    try:
        name = load_anime(row)
        print(f'Anime {name} successfully loaded...')
    except Exception as e:
        print('An exception during anime loading occurred: {}\n {}'.format(e, traceback.format_exc()))


class Command(BaseCommand):
    help = 'Loads anime data from csv file.'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str)
        parser.add_argument('max_workers', nargs=1, type=int)

    def handle(self, *args, **options):
        Path(base_path).mkdir(parents=True, exist_ok=True)
        print(options)
        with open(options['filename'][0], newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            next(spamreader, None)  # skip header
            max_workers = options['max_workers'][0]
            while True:
                worker_data = [next(spamreader, None) for _i in range(max_workers * 10)]
                with ProcessPoolExecutor(max_workers=max_workers) as executor:
                    list(executor.map(worker_job, worker_data))
