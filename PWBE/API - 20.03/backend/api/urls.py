from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.get_event),  
    path('eventos/by_id/<int:pk>/', views.get_event_by_id), 
    path('eventos/proximos/', views.get_upcoming_events), 
    path('eventos/post/', views.create_event),  
    path('eventos/update/<int:pk>/', views.update_event),  
    path('eventos/delete/<int:pk>/', views.delete_event),  
]
