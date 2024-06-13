from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('Donation',views.Donation, name="Donation"),
    path('signin',views.signin, name="signin"),
    path('logout',views.signout, name="logout"),
    path('signup',views.signup, name="signup"),
    path('about', views.About, name="About"),
    path('causes', views.Causes, name="Causes"),
    path('volunteer', views.Volunteer, name="Volunteer"),
    path('events', views.Events, name="Events"),
    path('contact', views.Contact, name="Contact"),
    path('all_volunteers', views.all_volunteers, name="all_volunteers"),
    path('search', views.search_volunteers, name = "search"),

    path('volunteers/<int:emp_id>/', views.volunteer_details, name = "details"),
    path('volunteers/delete/<int:emp_id>/', views.volunteer_delete, name = "delete"),
    path('volunteers/update/<int:emp_id>/', views.volunteer_update, name = "update"),
]
