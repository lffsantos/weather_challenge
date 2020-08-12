import pytest
from django.conf import settings

from weather.services import format_output_data, should_use_umbrella


def test_format_output_data():
    days = [1597503600, 1597590000, 1597762800]
    result = format_output_data(days)
    assert result == "You should take an umbrella in these days: Saturday, Sunday and Tuesday"


@pytest.mark.parametrize("humidity,humidity_condition, expected", [
    (50, 70, False), (70, 70, False), (70.5, 70, True), (80, 70, True)
])
def test_should_use_umbrella(humidity, humidity_condition, expected):
    settings.HUMIDITY = humidity_condition
    assert should_use_umbrella(humidity) == expected
