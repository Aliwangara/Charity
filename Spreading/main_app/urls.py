from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    
    path('signin',views.signin, name="signin"),
    
    path('logout',views.signout, name="logout"),
    
    path('signup',views.signup, name="signup"),
    
    path('about', views.About, name="About"),
    
    path('causes', views.Causes, name="Causes"),
    
    path('volunteer', views.Volunteer, name="Volunteer"),
    
    path('map', views.map, name = "map"),
    
    path('add', views.add_volunteer, name="add"),
    
    path('add_images', views.add_images, name="add_images"),
    
    path('events', views.Events, name="Events"),
    
    path('testimonies', views.testimonies, name="testimonies"),
    
    path('contact', views.Contact, name="Contact"),
    
    path('all_volunteers', views.all_volunteers, name="all_volunteers"),
    
    path('search', views.search_volunteers, name = "search"),
    
    
    path('testimonies/delete/<int:testimonies_id>/', views.testimonies_delete, name='testimonies_delete'),
    
    path('events/delete/<int:events_id>/', views.events_delete, name='events_delete'),
    
    path('cause/delete/<int:cause_id>/', views.cause_delete, name='cause_delete'),
    
    path('more_causes/<int:pk>', views.more_causes, name="more_causes"),
    
    path('image/delete/<int:image_id>/', views.delete_image, name='delete_image'),
    
    path('information/<int:pk>', views.information, name = "information"),
    
    path('volunteers/<int:emp_id>/', views.volunteer_details, name = "details"),
    
    path('volunteers/delete/<int:emp_id>/', views.volunteer_delete, name = "delete"),
    
    path('volunteers/update/<int:emp_id>/', views.volunteer_update, name = "update"),
]
