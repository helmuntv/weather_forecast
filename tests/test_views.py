import pytest
import django
from django.test import RequestFactory
from weather.views import IndexView


@pytest.mark.asyncio
async def test_get_weather_data_success():
    # Configuración del caso de prueba exitoso
    city = "new york"

    view = IndexView()
    response = await view.get_weather_data(city)

    assert response['city'] == "New York"


@pytest.mark.asyncio
async def test_get_weather_data_failure():
    # Configuración del caso de prueba de fallo
    city = "Invalid City"

    view = IndexView()
    response = await view.get_weather_data(city)

    assert response == {'error_message': 'Error getting weather data. Please check the city entered.'}


@pytest.mark.asyncio
async def test_post_request():
    django.setup()
    # Configuración del caso de prueba de solicitud POST
    factory = RequestFactory()
    request = factory.post({'city': 'bogota'})
    view = IndexView()
    view.request = request

    response = await view.post(request)

    assert response.status_code == 200
