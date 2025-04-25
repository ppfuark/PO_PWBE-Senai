from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subject, Teacher, RoomReservation
from .serializers import SubjectSerializer, TeacherSerializer, RoomReservationSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def create(self, serializer):
        if serializer.validated_data['name'].strip() == "":
            raise serializer.ValidationError("Name cannot be empty")
        serializer.save()
        
class SubjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [IsAuthenticated] 
    
    def put(self, request, *args, **kwargs):
        name = self.request.query_params.get('name')
        if len(name.strip()) < 2:
            raise ValidationError({"name": "Name must have at least 2 characters."})
        return super().put(request, *args, **kwargs)
    