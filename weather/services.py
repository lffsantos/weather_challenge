import logging

import requests
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from weather.models import City

logger = logging.getLogger(__name__)


class ForecastWeather:

    def __init__(self):
        self.api_url = settings.OPENWEATHER_API
        self.APPID = settings.APPID

    def days_for_use_umbrella(self, city_code):
        lat, lon = self.get_city_coordinates_by_code(city_code)
        response = self.request_daily_forecast_for_7_days(lat, lon)
        days = self.get_days_for_use_umbrella_in_next_5_days(response)
        return self.format_output_data(days)

    def request_daily_forecast_for_7_days(self, latitude, longitude):
        """
        https://openweathermap.org/api/one-call-api#how

        :param latitude (str)
        :param longitude (str)

        """
        url = f'{self.api_url}onecall?lat={latitude}&lon={longitude}&exclude=current,minutely,hourly&APPID={self.APPID}'
        data = self.call_api(url)
        return data

    def call_api(self, url):
        try:
            logger.info(f"call url {url}")
            r = requests.get(url, timeout=10)
            r.raise_for_status()
        except requests.exceptions.ConnectionError as error:
            logger.error(error)
            raise error
        except requests.exceptions.HTTPError as error:
            logger.error(error)
            if error.response.status_code == 401:
                raise error
            raise error
        except Exception as error:
            logger.error(error)
            raise error

        return r.json()

    def should_use_umbrella(self, humidity):
        """ Verify if should be used an umbrella if humidity more greater than configured"""
        return True if humidity > float(settings.HUMIDITY) else False

    def format_output_data(self, days):
        """
        Receive a list of timestamp and return a readable message for user
        :param days (list): list of timestamp
        """
        if not days:
            return f"You won't need an umbrella for the next few days"

        days = [datetime.fromtimestamp(d).strftime('%A') for d in days]
        if len(days) == 1:
            return f'You should take an umbrella in these days: {days[0]}'

        str_days = ', '.join(days[:-1])
        if len(days) >= 2:
            str_days += ' and ' + days[-1]

        return f'You should take an umbrella in these days: {str_days}'

    def get_city_coordinates_by_code(self, code):
        """
        Receive a code of city and return coordinates

        :param code (int): code of city
        :return (lat, lon):
        """
        try:
            city = City.objects.get(code=code)
        except ObjectDoesNotExist as error:
            raise error

        return city.latitude, city.longitude

    def get_days_for_use_umbrella_in_next_5_days(self, data):
        """
        Receive a list of daily information weather and return a list of timestamp for use umbrella
        :param data (dict): contain values related to weather included them  ("dt" -> timestamp) and ("humidity")
        :return: days (list) list of timestamp
        """
        return [d['dt'] for d in data['daily'][1:6] if self.should_use_umbrella(d['humidity'])]
