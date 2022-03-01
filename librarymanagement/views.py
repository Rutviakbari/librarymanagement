from lib2to3.pgen2.pgen import generate_grammar
from django.shortcuts import render

from rest_framework import generics
from librarymanagement import serializers

from librarymanagement.models import Book
from librarymanagement.serializers import BookSerializer

class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




