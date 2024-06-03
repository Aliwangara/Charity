from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('Donation',views.Donation, name="Donation"),
    path('signin',views.signin, name="Signin"),
    path('logout',views.signout, name="logout"),
]