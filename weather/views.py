from django.shortcuts import render

from weather.models import Country


def index(request):
    return render(request, 'index.html', {"countries": Country.objects.all()})
