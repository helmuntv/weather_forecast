from django.shortcuts import render
from weather.apis.APICaller import APICaller
import os
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        template_name = "weather/index.html"
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        template_name = "weather/index.html"

        if request.method == 'POST':
            API_KEY = os.getenv('API_KEY')
            city    = request.POST.get('city')
            units   = 'metric'
            url     = os.getenv('URL_OPENWEATHER_API')
            query_params = 'q='+city+'&units='+units+'&appid='+API_KEY
            
            response = APICaller.api_call_get(url, query_params)        
            if response.status_code == 200:
                data = response.json()
                city = data['name']
                context = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                }
                return render(request, template_name, context)
            else:
                error_message = 'Error getting weather data. Please check the city entered.'
                return render(request, template_name, {'error_message': error_message})

        return render(request, template_name)
    
    
    #def get(self, request, *args, **kwargs):
    #    pass
        #return HttpResponseNotAllowed(['GET'])
        #return HttpResponseNotAllowed(['POST'])
