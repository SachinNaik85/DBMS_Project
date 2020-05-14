from django.urls import path
from search import views


urlpatterns = [
    path('', views.home, name="SearchPlace"),
    path('/booking_request', views.booking_request, name="booking page"),
    path('/<place_from_features>', views.features_home, name="search place"),
    path('/searchplace/booking_request', views.booking_request, name="booking request")
]
