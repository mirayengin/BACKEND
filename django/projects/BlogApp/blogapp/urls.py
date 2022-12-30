
from django.urls import path, include
from .views import CategoryCVS,CategoryDetailCVS,PostMVS
from rest_framework import routers


router = routers.DefaultRouter()
router.register("post", PostMVS)

urlpatterns = [
  #? cvs ile yazılım
    path('category/',CategoryCVS.as_view()),
    path('category/<int:pk>',CategoryDetailCVS.as_view()),
    # path('cat/',CategoryCreateCVS.as_view()),

    #! mvs ile yazılım
    # path('', include(router.urls)),

]

urlpatterns += router.urls
