from rest_framework import generics
from . import Review, ReviewSerializer




class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objetcs.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
