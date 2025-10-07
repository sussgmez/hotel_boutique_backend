from django.contrib import admin
from .models import Room, Reservation, RoomType, Guest


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
