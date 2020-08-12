import pytest
from django.conf import settings

from weather.services import ForecastWeather


@pytest.fixture
def forecast_weather():
    return ForecastWeather()


@pytest.mark.parametrize("days,expected", [
    ([1597503600, 1597590000, 1597762800], "You should take an umbrella in these days: Saturday, Sunday and Tuesday"),
    ([1597503600, 1597590000], "You should take an umbrella in these days: Saturday and Sunday"),
    ([], "You won't need an umbrella for the next few days"),
])
def test_format_output_data(forecast_weather, days, expected):
    result = forecast_weather.format_output_data(days)
    assert result == expected


@pytest.mark.parametrize("humidity,humidity_condition, expected", [
    (50, 70, False), (70, 70, False), (70.5, 70, True), (80, 70, True)
])
def test_should_use_umbrella(forecast_weather, humidity, humidity_condition, expected):
    settings.HUMIDITY = humidity_condition
    assert forecast_weather.should_use_umbrella(humidity) == expected


def test_get_days_for_use_umbrella_in_next_5_days(forecast_weather, daily_forecast_for_7_days_sample):
    days = forecast_weather.get_days_for_use_umbrella_in_next_5_days(daily_forecast_for_7_days_sample)
    assert days == [1597687200]
