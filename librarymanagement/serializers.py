
from rest_framework import serializers
from librarymanagement.models import Book

class adminSerializer(serializers.ModelSerializer):
 class Meta:
     model = Book
     fields = ['title','author','isbn','publisher']