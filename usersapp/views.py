import email
from re import U
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer
from .models import note, User


"""
Views for the user API.
"""


from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except note.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        email_user = request.user
        print(email_user)
        user = User.objects.get(email=email_user)
        if user.is_superuser:
            users = User.objects.all()
        else:
            return Response({'error':'You do not have access ,You are not superuser'})
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)




class NotetList(APIView):

    """
    List all Notes, or create a new Note.
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return note.objects.get(pk=pk)
        except note.DoesNotExist:
            raise Http404


    def get(self, request, format=None):

        try:
            # Notes = note.objects.filter(user = user_pk)
            Notes = note.objects.filter(user=request.user)
        except note.DoesNotExist:
            return Http404

        serializer = NoteSerializer(Notes, many=True)


        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        user = User.objects.get(email=user)
        request.data['user'] = user.pk

        serializer = NoteSerializer(data=request.data)
        

        #print(serializer)
        if serializer.is_valid():
            
            serializer.save()
            return Response({'name':'Response OK'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        Note = self.get_object(pk)
        serializer = NoteSerializer(Note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Note = self.get_object(pk)
        Note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



########################################################################################################




class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
