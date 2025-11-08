# LibraryProject/relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This variable is used in the template

# Optional: Example of using get_object_or_404 (if you want to use a function-based detail view)
def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})
