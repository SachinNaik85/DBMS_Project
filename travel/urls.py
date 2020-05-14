from django.urls import path
from travel import views

urlpatterns = [
    path('', views.home, name="HomePage"),
    path('login', views.login, name="LoginPage"),
    path('signup', views.signup, name="SgininPage"),
    path('logout', views.logout, name="Homepage"),
    path('reset_password', views.reset_password, name="reset_page"),
    path('change_password', views.change_password, name="change_password")
]
