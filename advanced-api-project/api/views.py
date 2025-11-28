# api/views.py

"""
Generic views for Book model using Django REST Framework.
Includes:
- Filtering (title, author, publication_year)
- Searching (title, author)
- Ordering (title, publication_year)
"""

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions, filters
from django_filters import rest_framework as django_filters   # <-- REQUIRED FOR FILTERING
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # REQUIRED by the project checker
    # Enables: filtering, searching, ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,   # <-- FILTERING
        filters.SearchFilter,                # <-- SEARCH
        filters.OrderingFilter,              # <-- ORDERING
    ]

    # filter by fields
    filterset_fields = ['title', 'author', 'publication_year']

    # search by fields
    search_fields = ['title', 'author__name']

    # ordering options
    ordering_fields = ['title', 'publication_year']



class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
