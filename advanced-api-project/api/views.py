# api/views.py
"""
Generic views for Book model using Django REST Framework.
This file defines combined views:
- BookListCreateView: list all books (GET) or create a book (POST)
- BookDetailView: retrieve, update, or delete a single book by ID

Permissions:
- GET requests: anyone can access
- POST, PUT, PATCH, DELETE: only authenticated users
"""

from rest_framework import generics, permissions, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: list all books (with filtering, search, ordering)
    POST: create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'published_year', 'publication_year']  # temporary include publication_year
    ordering_fields = ['title', 'published_year', 'publication_year']
    search_fields = ['title', 'author__name']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: retrieve a single book
    PUT/PATCH: update book (authenticated users only)
    DELETE: delete book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
