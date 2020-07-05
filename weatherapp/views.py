from django.shortcuts import render
from django.http import Http404
import json
import urllib.request
# Create your views here.

def weather(request):

    if request.method == "POST":
        city = request.POST['city']
        
        weather_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0ba95c7453833259c670c7cf3dc8d30c').read()
    
        list_of_data = json.loads(weather_url)
    
        context = {
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']) + ' hPA', 
            "humidity": str(list_of_data['main']['humidity']) + "%",
            "wind":str(list_of_data['wind']['speed'])+ " m/s",
            "weather":str(list_of_data['weather'][0]['main'])

            }

    else:
        context = {}

    return render(request, "weatherapp/weather.html", context)