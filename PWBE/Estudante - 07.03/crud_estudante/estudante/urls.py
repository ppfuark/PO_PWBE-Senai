from django.urls import path
from . import views
 
urlpatterns = [
    path('list', views.list_all),
    path('<int:pk>', views.student_by_id),
    path('create', views.create_student),
    path('update/<int:pk>', views.update_student),
    path('delete/<int:pk>', views.delete_student),
    path('print/<str:text>', views.print_text),
]