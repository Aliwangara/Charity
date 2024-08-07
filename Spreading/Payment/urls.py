from django.urls import path
from . import views

urlpatterns = [
   path('Donation',views.Donation, name="Donation"),
   path('callback', views.callback, name='callback'),
   path('card',views.card, name="card"),


]
