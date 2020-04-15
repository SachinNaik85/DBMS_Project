from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="SearchPage"),
    path('/booking_request', views.booking_request, name="booking page")
]
