from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer
from .models import note


class NotetList(APIView):

    """
    List all Notes, or create a new Note.
    """
    def get(self, request, format=None):
        Notes = note.objects.all()
        print(' start Notes *********************************')
        print('type :' + str(type(Notes)))
        print(Notes.get(id=1))
        print(' End Notes *********************************')

        serializer = NoteSerializer(Notes, many=True)
        print('serializer :' + str(type(serializer)))
        print('serializer :' + str(type(serializer.data)))

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'name':'Response OK'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
