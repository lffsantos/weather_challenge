import requests
from datetime import datetime

from django.conf import settings


WEATHER_API = settings.OPENWEATHER_API
APPID = settings.APPID


def request_daily_forecast_for_7_days(latitude, longitude):
    """
    https://openweathermap.org/api/one-call-api#how

    :param latitude (str)
    :param longitude (str)

    """
    url = f'{WEATHER_API}?onecall=lat={latitude}&long={longitude}&exclude=current,minutely,hourly&appid={APPID}'
    data = call_api(url)
    return data


def call_api(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.ConnectionError as error:
        raise error
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            raise error

    except Exception as error:
        raise error

    return r.json()


def should_use_umbrella(humidity):
    """ Verify if should be used an umbrella if humidity more greater than configured"""
    return True if humidity > settings.HUMIDITY else False


def format_output_data(days):
    """
    Receive a list of timestamp and return a readable message for user
    :param days (list): list of timestamp
    """
    str_days = [datetime.fromtimestamp(d).strftime('%A') for d in days]
    str_days = ', '.join(str_days[:-1]) + ' and ' + str_days[-1]

    return f'You should take an umbrella in these days: {str_days}'
