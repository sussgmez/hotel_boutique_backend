from rest_framework import routers
from .views import GuestViewSet, RoomViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r"guests", GuestViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"reservations", ReservationViewSet)

urlpatterns = router.urls
