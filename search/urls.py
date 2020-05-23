from django.urls import path, re_path
from search import views


urlpatterns = [
    path('', views.home, name="SearchPlace"),
    re_path(r'^/(?P<feature_name>[a-zA-Z]+)$', views.features_home, name="search place"),
    path('/bus&hotel', views.booking_request, name="booking_page"),
    path('/search/bus&hotel', views.booking_request, name="booking request"),
    re_path(r'^/search/(?P<hotel_name>[a-zA-Z_]+)$', views.book_hotel, name="book_hotel"),
    path('/search/confirm_bus/<busname>', views.book_bus),
    re_path(r'^/search/(?P<busname>[a-zA-Z0-9]+)$', views.book_bus, name="book_bus"),
    path('/search/confirm_hotel/<hotel_name>', views.book_hotel)
]
