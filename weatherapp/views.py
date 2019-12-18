from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    appid = '80852c672a959c2bc2837c7037ac1f58'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.order_by('-pk')[0:1]

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"],
            'pressure': res["main"]["pressure"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weatherapp/index.html', context)