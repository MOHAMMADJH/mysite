from this import s
from django.shortcuts import render


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from .serializers import (MovieSerializer, GenresSerializer,
 ProductionCompaniesSerializer,ProductionCountriesSerializer,
  SpokenLanguagesSerializer)
from ..models import (Movie,
Production_countries,Production_companies,
Spoken_languages,Genres)
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from usersapp.models import User
from django.contrib.auth import get_user_model


@api_view(['GET','POST'])
def hello_world(request):
    return Response({"message": "Hello, world!"})






@api_view(['GET'])
def movie_list(request):
    if request.method == "GET":
        try:
            movies = Movie.objects.all()
        except Movie.DoesNotExist:
            return Http404
    
        seriarlizer = MovieSerializer(movies ,many=True)
        return Response(seriarlizer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_movie(request):
    email_user = request.user
    user = User.objects.get(email=email_user)
    if user.is_superuser:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'name':'Response OK'}, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors})
    return Response({'error':'You do not have access ,You are not superuser'})

        
       


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def genres_list(request):
    if request.method == "GET":
        try:
            genres = Genres.objects.all()
        except Movie.DoesNotExist:
            return Http404
    
        seriarlizer = GenresSerializer(genres ,many=True)
        return Response(seriarlizer.data)

    if request.method == "POST":
        email_user = request.user
        user = User.objects.get(email=email_user)

        if not request.data: 
            return Response({'error':'No Data'})
        else:    
            if user.is_superuser:
                serializer = GenresSerializer(data=request.data, many=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"OK":serializer.data}, status=status.HTTP_201_CREATED)
                return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            return Response({'error':'You do not have access ,You are not superuser'})
               
           

       


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def production_companies_list(request):
    if request.method == "GET":
        try:
            production_companiess = Production_companies.objects.all()
        except Movie.DoesNotExist:
            return Http404
    
        seriarlizer = ProductionCompaniesSerializer(production_companiess ,many=True)
        return Response(seriarlizer.data)

    if request.method == "POST":
        email_user = request.user
        user = User.objects.get(email=email_user)
        if user.is_superuser:
            serializer = ProductionCompaniesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'name':'Response OK'}, status=status.HTTP_201_CREATED)
            return Response({'error':serializer.errors})
        return Response({'error':'You do not have access ,You are not superuser'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def production_countries_list(request):
    if request.method == "GET":
        try:
            production_countriess = Production_countries.objects.all()
        except Movie.DoesNotExist:
            return Http404
    
        seriarlizer = ProductionCountriesSerializer(production_countriess ,many=True)
        return Response(seriarlizer.data)
    if request.method == "POST":
        email_user = request.user
        user = User.objects.get(email=email_user)
        if user.is_superuser:
            serializer = ProductionCountriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'name':'Response OK'}, status=status.HTTP_201_CREATED)
            return Response({'error':serializer.errors})
        return Response({'error':'You do not have access ,You are not superuser'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def spoken_languages_list(request):
    if request.method == "GET":
        try:
            spoken_languages = Spoken_languages.objects.all()
        except Movie.DoesNotExist:
            return Http404
    
        seriarlizer = SpokenLanguagesSerializer(spoken_languages ,many=True)
        return Response(seriarlizer.data)
    if request.method == "POST":
        email_user = request.user
        user = User.objects.get(email=email_user)
        if user.is_superuser:
            serializer = SpokenLanguagesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'name':'Response OK'}, status=status.HTTP_201_CREATED)
            return Response({'error':serializer.errors})
        return Response({'error':'You do not have access ,You are not superuser'})

        

