from django.urls import path
from . import views

urlpatterns = [
   path('Donation',views.Donation, name="Donation"),

]
