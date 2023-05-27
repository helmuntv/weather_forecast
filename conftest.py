import pytest
from django.conf import settings
import os

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_forecast.settings')
    settings.DEBUG = False 
