from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from datetime import date, timedelta

from .models import Event
from .serializers import EventSerializer


@api_view(['GET'])
def get_event(request):
    category = request.GET.get("category")
    day = request.GET.get("day")
    quantity = request.GET.get("quantity")
    ordering = request.GET.get("ordering", "day")  

    events = Event.objects.all()

    if category:
        events = events.filter(category=category)
    if day:
        events = events.filter(day=day)
    if quantity:
        try:
            quantity = int(quantity)
            events = events[:quantity]  # Correct slicing
        except ValueError:
            return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)

    events = events.order_by(ordering)  

    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_event_by_id(request, pk):
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)


@api_view(['GET'])
def get_upcoming_events(request):
    today = date.today()
    next_week = today + timedelta(days=7)
    events = Event.objects.filter(day__range=[today, next_week]).order_by("day")
    
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
