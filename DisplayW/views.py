from django.shortcuts import render

# Create your views here.
# weather_app/display/views.py
from datetime import datetime
import requests

API_KEY = '46860ed59a8a0f0f767051e52b6cca44'  # API KEY of own location
CITY = 'Kathmandu'  # City or place where am I

def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        return temperature
    else:
        return 'Error'

def index(request):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    current_date = now.strftime('%Y-%m-%d')
    temperature = get_weather()

    context = {
        'current_time': current_time,
        'current_date': current_date,
        'temperature': temperature,
    }
    return render(request, 'DisplayW/index.html', context)
