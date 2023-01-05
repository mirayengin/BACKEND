from django.urls import path,include
from rest_framework import routers
from .views import FlightView

router = routers.DefaultRouter()
router.register("flights", FlightView)


# urlpatterns = [
#     path("", router.urls),



# ]

urlpatterns = router.urls