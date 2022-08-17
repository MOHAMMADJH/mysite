"""
URL mappings for the user API.
"""
from django.urls import path, include

from .views import (movie_list, genres_list,
            production_companies_list,
            production_countries_list,
            spoken_languages_list,
            add_movie,
            hello_world)


"""

All Endpoint Movies OP API
list Working GET & POST method
GET permission For All Put Post For Is stuff User


"""


urlpatterns = [

    path('hi/', hello_world),
    path('movielist/', movie_list),
    path('spokenlanguageslist/', spoken_languages_list),
    path('productioncountrieslist/', production_countries_list),
    path('productioncompanieslist/', production_companies_list),
    path('genreslist/', genres_list),
    path('addmovie/', add_movie),
]
