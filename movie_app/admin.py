from re import I
from django.contrib import admin
from movie_app.models import Genres, Movie, Production_companies, Production_countries, Spoken_languages
from movie_app.models import Test
admin.site.register(Genres)
admin.site.register(Production_companies)
admin.site.register(Production_countries)
admin.site.register(Spoken_languages)
admin.site.register(Movie)
admin.site.register(Test)