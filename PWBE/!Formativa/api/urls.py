from django.urls import path 
from . import views

urlpatterns = [
    path('subject/', views.SubjectListCreateAPIView.as_view(), name="subject-list-create"),
    path('subject/<int:pk>/', views.SubjectRetrieveUpdateDestroyAPIView.as_view(), name="subject-detail"),
]