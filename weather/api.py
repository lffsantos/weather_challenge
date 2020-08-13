import json

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from weather import services
from weather.filters import CityFilter
from weather.models import City, Country
from weather.serializers import CitySerializer, CountrySerializer
from weather.services import ForecastWeather


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
        forecast_weather = ForecastWeather()
        try:
            response = forecast_weather.days_for_use_umbrella(city_code)
        except ObjectDoesNotExist:
            raise NotFound(detail="City not found", code=404)
        except requests.exceptions.HTTPError as error:
            return Response(str(error), status=error.response.status_code)
        except Exception as error:
            return Response(str(error))

        return Response(response)
