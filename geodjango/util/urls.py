from django.urls import path

from . import views

urlpatterns = [
    path("maps_api_key/", views.mapsApiKey.as_view()),
]