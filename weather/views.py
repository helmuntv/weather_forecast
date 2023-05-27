from django.shortcuts import render
from weather.apis.APICaller import APICaller
import os
from django.views import View


class IndexView(View):
    template_name = "weather/index.html"

    async def get_weather_data(self, city):
        API_KEY = os.getenv('API_KEY')
        units = 'metric'
        url = os.getenv('URL_OPENWEATHER_API')
        query_params = f'q={city}&units={units}&appid={API_KEY}'

        response = await APICaller.api_call_get(url, query_params)
        
        if response.status_code == 200:
            data = response.json()

            icon_name = data['weather'][0]['icon']
            url = 'http://openweathermap.org/img/wn/'
            query_params_icon = f'{icon_name}@2x.png'
            icon_api = url+query_params_icon

            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': icon_api
            }
        else:
            return {'error_message': 'Error getting weather data. Please check the city entered.'}

    
    async def get(self, request, *args, **kwargs):
        context = await self.get_weather_data("new york")
        return render(request, self.template_name, context)

    
    async def post(self, request, *args, **kwargs):
        city = request.POST.get('city')
        context = await self.get_weather_data(city)
        return render(request, self.template_name, context)
