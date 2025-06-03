from django.urls import path
from book import views


urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]
