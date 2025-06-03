from rest_framework import generics
from . import Book, BookSerializer




class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objetcs.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
