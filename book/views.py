from rest_framework import generics
from . import Book




class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objetcs.all()
    serializer_class = None

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = None