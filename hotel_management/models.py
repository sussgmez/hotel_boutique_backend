from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save


class RoomType(models.Model):
    name = models.CharField(_("Tipo de habitación"), max_length=50)
    price = models.FloatField(_("Precio"), validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} ({self.price}$)"


class Room(models.Model):
    STATUS_CHOICES = [
        (1, "Disponible"),
        (2, "Ocupada"),
        (3, "En mantenimiento"),
    ]

    number = models.CharField(_("Número"), max_length=20)
    room_type = models.ForeignKey(
        RoomType, verbose_name=_("Tipo de habitación"), on_delete=models.CASCADE
    )
    status = models.SmallIntegerField(_("Status"), choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")
        unique_together = [["number", "room_type"]]

    def __str__(self):
        return f"{self.number} - {self.room_type.name}"


class Guest(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ("V", "V"),
        ("E", "E"),
        ("J", "J"),
        ("G", "G"),
    ]

    document_type = models.CharField(
        _("Documento"), max_length=1, choices=DOCUMENT_TYPE_CHOICES
    )
    document_number = models.PositiveIntegerField(_("Número de docuemento"))
    name = models.CharField(_("Nombre"), max_length=200)
    phone_number = models.CharField(_("Número de teléfono"), max_length=50)
    email = models.EmailField(_("Correo electrónico"), max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [["document_type", "document_number"]]


class Reservation(models.Model):
    guest = models.ForeignKey(
        Guest,
        verbose_name=_("Huésped"),
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    room = models.ForeignKey(
        Room,
        verbose_name=_("Habitación"),
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    checkin_date = models.DateField(_("Fecha de entrada"))
    checkout_date = models.DateField(_("Fecha de salida"))
    active = models.BooleanField(_("Activa"), default=False)


@receiver(pre_save, sender=Reservation)
def reservation_pre_save_receiver(sender, instance, **kwargs):
    try:
        active_reservation = instance.room.reservations.get(active=True)
        active_reservation.active = False
        active_reservation.save()
    except:
        pass
