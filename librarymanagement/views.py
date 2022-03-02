

from rest_framework import viewsets
from .serializers import adminSerializer
from .models import Book

class BookviewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = adminSerializer


                
