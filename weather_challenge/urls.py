from django.contrib import admin
from django.urls import path, include

from weather.views import index

urlpatterns = [
    path('', index, name='report'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('weather.urls')),
]
