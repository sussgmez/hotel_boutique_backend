from django.shortcuts import render
from rest_framework import viewsets
from .models import Guest, Room, RoomType, Reservation
from .serializers import (
    GuestSerializer,
    RoomSerializer,
    ReservationSerializer,
    RoomTypeSerializer,
)


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by("status")
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.query_params.get("number"):
            queryset = queryset.filter(number=self.request.query_params.get("number"))

        return queryset


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
