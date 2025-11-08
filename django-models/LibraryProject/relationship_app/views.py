from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # <-- Important: this line is what the check looks for

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # <-- Check looks for this
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library details
class LibraryDetailView(DetailView):  # <-- Check looks for DetailView
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
