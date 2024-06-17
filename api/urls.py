from django.contrib import admin
from django.urls import path
# from .views import movie_list,movie_details
from .views import MovieListAV, MovieDetailsAV

urlpatterns = [
   path('v1/movies',MovieListAV.as_view(), name='movie-list'),
   path('v1/movies/<int:pk>', MovieDetailsAV.as_view(), name='movie-detail'),
]
