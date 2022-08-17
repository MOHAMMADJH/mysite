
from asyncore import read
from rest_framework import serializers
from ..models import Movie, Genres, Production_companies, Production_countries, Spoken_languages
from rest_framework import serializers
from django.contrib.auth import get_user_model

from djoser.serializers import UserCreateSerializer


class MovieSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['pk']


class GenresSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Genres
        fields = '__all__'
        read_only_fields = ['pk']

    def create(self, validated_data):
        return Genres.objects.create(**validated_data)

class ProductionCompaniesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Production_companies
        fields = '__all__'
        read_only_fields = ['pk']

class ProductionCountriesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Production_countries
        fields = '__all__'
        read_only_fields = ['pk']


class SpokenLanguagesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Spoken_languages
        fields = '__all__'
        read_only_fields = ['pk']