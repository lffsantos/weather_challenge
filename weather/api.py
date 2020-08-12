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
from weather.models import City
from weather.serializers import CitySerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
        A simple ViewSet for viewing cities.
        """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CityFilter


class WeatherViewSet(APIView):
    http_method_names = ['get']

    def get(self, request, city_code):
        try:
            lat, lon = services.get_city_coordinates_by_code(city_code)
        except ObjectDoesNotExist:
            raise NotFound(detail="City not found", code=404)

        try:
            request = services.request_daily_forecast_for_7_days(lat, lon)
        except requests.exceptions.HTTPError as error:
            return Response(str(error), status=error.response.status_code)
        except Exception as error:
            return Response(str(error))

        days = services.get_days_for_use_umbrella_in_next_5_days(request)

        return Response(services.format_output_data(days))
