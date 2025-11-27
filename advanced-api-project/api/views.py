# api/views.py
"""
Generic views for Book model using Django REST Framework.
This file defines separate generic views:
- BookListView:  returns list of all books (GET /books/)
- BookDetailView: returns a single book by id (GET /books/<pk>/)
- BookCreateView: creates a new book (POST /books/create/)
- BookUpdateView: updates an existing book (PUT/PATCH /books/<pk>/update/)
- BookDeleteView: deletes a book (DELETE /books/<pk>/delete/)

Permissions:
- List and Detail views are open (anyone can read).
- Create/Update/Delete require authentication (only logged in users).
"""

from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# Anyone can view the list, but we include filtering support for convenience.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # read-only for everyone
    # allow simple search (e.g., ?search=Harry) and ordering (e.g., ?ordering=publication_year)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']

# Retrieve a single book by primary key (id). Anyone can view.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book. Only authenticated users can create.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Optional: you can customize how an object is saved here
    def perform_create(self, serializer):
        # For now we just save normally. You could attach the current user here if desired.
        serializer.save()

# Update an existing book. Only authenticated users can update.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Use put/patch to update. Validation runs automatically via serializer.validate_*

# Delete a book. Only authenticated users can delete.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
