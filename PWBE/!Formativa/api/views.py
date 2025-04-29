from .models import Subject, Teacher, RoomReservation
from .serializers import SubjectSerializer, TeacherSerializer, RoomReservationSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


# ====================================== Subjects ============================================

class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [IsAuthenticated()]
    #     return [IsManager()]
        
class SubjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    # def get_permissions(self):
    #     return [IsManager()

# ====================================== Subjects ============================================


# ====================================== Teacher ============================================

class TeacherListCreateAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [IsAuthenticated]
    #     return [IsManager()]

class TeacherRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    # def get_permissions(self):
    #     return [IsManager()]

# ====================================== Teacher ============================================


# ====================================== Teacher ============================================

class RoomReservationListCreateAPIView(ListCreateAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomReservationSerializer
    
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [IsAuthenticated]
    #     return [IsManager()]
    
class RoomReservationRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    print("nn")
    # def get_permissions(self):
    #     return [IsManager()]


# ====================================== Teacher ============================================