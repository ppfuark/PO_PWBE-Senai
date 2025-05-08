from django.urls import path 
from . import views

urlpatterns = [
    # Subject
    path('subject/', views.SubjectListCreateAPIView.as_view(), name="subject-list-create"),
    path('subject/<int:pk>/', views.SubjectRetrieveUpdateDestroyAPIView.as_view(), name="subject-detail"),

    # Teacher
    path('teacher/', views.TeacherListCreateAPIView.as_view(), name="teacher-list-create"),
    path('teacher/<int:pk>/', views.TeacherRetrieveUpdateDestroyAPIView.as_view(), name="teacher-detail"),

    # RoomReservation
    path('room-reservation/', views.RoomReservationListCreateAPIView.as_view(), name="room-reservation-list-create"),
    path('room-reservation/<int:pk>/', views.RoomReservationRetrieveUpdateDestroyAPIView.as_view(), name="room-reservation-detail"),
]
