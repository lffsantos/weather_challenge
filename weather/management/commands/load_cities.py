import json
import os

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from weather.models import City
from weather_challenge import settings


class Command(BaseCommand):

    def handle(self, **options):
        path_dir = os.path.join(settings.BASE_DIR, 'static')
        city_file = os.path.join(path_dir, 'city.list.json')
        with open(city_file) as json_file:
            data = json.load(json_file)
            for line in data:
                code, name, state, country = line['id'], line['name'], line['state'], line['country']
                latitude, longitude = line['coord']['lat'], line['coord']['lon']
                try:
                    City.objects.create(
                        code=code, name=name, state=state, country=country, latitude=latitude, longitude=longitude
                    )
                except IntegrityError:
                    print("City already exists... skip")

                print(f'{name} - registered')

        print("All cities have been registered")
