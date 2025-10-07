from rest_framework import serializers
from .models import Guest, Room, RoomType, Reservation


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = [
            "id",
            "document_type",
            "document_number",
            "name",
            "phone_number",
            "email",
        ]


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            "id",
            "guest",
            "room",
            "checkin_date",
            "checkout_date",
            "active",
        ]


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = [
            "id",
            "name",
            "price",
        ]


class RoomSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)
    active_reservation = serializers.SerializerMethodField()
    room_type_data = RoomTypeSerializer(read_only=True, source="room_type")
    status_display = serializers.ReadOnlyField(source="get_status_display")

    class Meta:
        model = Room
        fields = [
            "id",
            "number",
            "room_type",
            "room_type_data",
            "status",
            "status_display",
            "reservations",
            "active_reservation",
        ]

    def get_active_reservation(self, obj):
        try:
            return ReservationSerializer(obj.reservations.get(active=True)).data
        except:
            return None
