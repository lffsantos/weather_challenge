from datetime import datetime

from django.conf import settings


def call_forecast_weather_api():
    return {}


def should_use_umbrella(humidity):
    return True if humidity > settings.HUMIDITY else False


def format_output_data(days: list):

    str_days = [datetime.fromtimestamp(d).strftime('%A') for d in days]
    str_days = ', '.join(str_days[:-1]) + ' and ' + str_days[-1]

    return f'You should take an umbrella in these days: {str_days}'
