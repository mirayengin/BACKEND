from django.urls import path
from .views import TutorialMVS

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#! bu r dökümastasyonda var o yüzden yazdık
router.register(r"tutorials", TutorialMVS)
urlpatterns = router.urls

# urlpatterns = [   path(), ]