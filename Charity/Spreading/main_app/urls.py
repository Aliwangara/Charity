from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('Donation',views.Donation, name="Donation"),
    path('signin',views.signin, name="Signin"),
    path('logout',views.signout, name="logout"),
    path('signup',views.signup, name="signup"),
    path('about', views.About, name="About"),
    path('causes', views.Causes, name="Causes"),
    path('volunteer', views.Volunteer, name="Volunteer"),
    path('events', views.Events, name="Events"),
    path('contact', views.Contact, name="Contact")
]
