from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="HomePage"),
    path('login', views.login, name="LoginPage"),
    path('signup', views.signup, name="SgininPage"),
    path('signed_up', views.signed_up, name="HomePage"),
]
