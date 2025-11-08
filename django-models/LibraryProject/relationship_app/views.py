# LibraryProject/relationship_app/views.py

# Imports
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Show details for a specific library
class LibraryDetailView(DetailView):
    model = Library                # the model to use
    template_name = 'relationship_app/library_detail.html'  # template file
    context_object_name = 'library'  # name to use in the template
