from django.urls import path
from .views import get_artistList,post_artistList,artist_list,artist_detail


urlpatterns = [
    # path('', artist_list),
    path('get/', get_artistList),
    path('post/', post_artistList),
    path('artist/', artist_list),
    path('artist/<int:pk>', artist_detail),
]