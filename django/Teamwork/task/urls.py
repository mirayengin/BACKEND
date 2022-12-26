from django.urls import path
from .views import (
    get_artist_list,
    post_artist_list,
    artist_list,artist_detail,
    artist_update
    )


urlpatterns = [
    # path('', artist_list),
    path('/get', get_artist_list),
    path('/post', post_artist_list),
    path('/artist/', artist_list),
    path('/<int:pk>', artist_detail),
    path('/put/<int:pk>', artist_update),
]