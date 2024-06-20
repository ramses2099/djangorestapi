from django.contrib import admin
from django.urls import path
# from .views import movie_list,movie_details
from .views import WatchListAV, WatchDetailsAV,StreamPlatformListAV,StreamPlatformDetailsAV

urlpatterns = [
   path('v1/watchlist',WatchListAV.as_view(), name='watch-list'),
   path('v1/watchlist/<int:pk>', WatchDetailsAV.as_view(), name='watch-list-detail'),
   path('v1/streamplatformlist',StreamPlatformListAV.as_view(), name='stream-platforms-list'),
   path('v1/streamplatformlist/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream-platforms-detail'),
]
