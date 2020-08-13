from rest_framework.routers import DefaultRouter
from django.urls import path
from weather.api import CityViewSet, WeatherViewSet, CountryViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet, 'city')
router.register(r'countries', CountryViewSet, 'country')


urlpatterns = router.urls
urlpatterns += [
    path('weather/<int:city_code>', WeatherViewSet.as_view(), name='obtain-weather'),
]
