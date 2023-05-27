from django.contrib import admin
from django.urls import include, path
from weather.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path("__reload__/", include("django_browser_reload.urls")),
]
