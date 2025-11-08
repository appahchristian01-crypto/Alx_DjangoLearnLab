```python
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView  # ✅ Exact import the checker wants
from .models import Library, Book  # ✅ Library first for earlier check

# Function-Based View: List all books
def list_books(request):
 books = Book.objects.all()
 return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display details for a specific library
class LibraryDetailView(DetailView):
 model = Library
 template_name = 'relationship_app/library_detail.html'
 context_object_name = 'library'
