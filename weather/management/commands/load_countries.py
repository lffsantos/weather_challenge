import json
import os

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from weather.models import Country
from weather_challenge import settings


class Command(BaseCommand):

    def handle(self, **options):
        path_dir = os.path.join(settings.BASE_DIR, 'static')
        city_file = os.path.join(path_dir, 'country.list.json')
        with open(city_file) as json_file:
            data = json.load(json_file)
            for line in data:
                initials, name = line['sigla'], line['nome_pais_int']
                try:
                    Country.objects.create(initials=initials, name=name)
                except IntegrityError:
                    print("Country already exists... skip")

                print(f'{name} - registered')

        print("All countries have been registered")
