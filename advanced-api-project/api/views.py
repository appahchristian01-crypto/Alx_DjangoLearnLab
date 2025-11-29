from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books (anyone can access)
    POST: Create a new book (authenticated users only)
    Supports filtering, ordering, and search
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Filters and search
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'published_year']  # exact filtering
    ordering_fields = ['title', 'published_year']             # allow ordering
    search_fields = ['title', 'author__name']                 # allow search by title or author name

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book details (anyone can access)
    PUT/PATCH/DELETE: Only authenticated users can modify or delete
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
