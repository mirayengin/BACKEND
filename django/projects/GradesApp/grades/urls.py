
from django.urls import path
from .views import TeacherMVS, LessonMVS,StudentsMVS, GradeMVS
from rest_framework import routers

# #? for images
# from django.conf import settings
# from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register("teacher", TeacherMVS)
router.register("lesson", LessonMVS)
router.register("students", StudentsMVS)
router.register("grade", GradeMVS)


urlpatterns = router.urls