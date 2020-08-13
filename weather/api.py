import logging

import requests
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from weather.filters import CityFilter
from weather.models import City, Country
from weather.serializers import CitySerializer, CountrySerializer
from weather.services import ForecastWeather

logger = logging.getLogger(__name__)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing cities.
        """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CityFilter


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing countries.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class WeatherViewSet(APIView):
    http_method_names = ['get']

    def get(self, request, city_code):
        cache_key = f'/weather/{city_code}'
        if cache.get(cache_key):
            logger.info(f"get {cache_key} from cache")
            return Response(cache.get(cache_key))

        forecast_weather = ForecastWeather()
        try:
            response = forecast_weather.days_for_use_umbrella(city_code)
        except ObjectDoesNotExist:
            logger.info(f"City not found city_code={city_code}")
            raise NotFound(detail="City not found", code=404)
        except requests.exceptions.HTTPError as error:
            logger.error(error)
            return Response(str(error), status=error.response.status_code)
        except Exception as error:
            logger.error(str(error))
            return Response(str(error))

        logger.info(f"add {cache_key} to cache")
        cache.set(cache_key, response, 60*60)
        return Response(response)
