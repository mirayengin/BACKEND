from django.urls import path,include
from rest_framework import routers
from .views import FlightView,ReservationView

router = routers.DefaultRouter()
router.register("flights", FlightView)
router.register("reservations", ReservationView)


# urlpatterns = [
#     path("", router.urls),



# ]

urlpatterns = router.urls