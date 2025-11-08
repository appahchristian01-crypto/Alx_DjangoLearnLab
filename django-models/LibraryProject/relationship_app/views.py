from django.contrib.auth.forms import UserCreationForm
from django. urls import reverse_lazy
from django. views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm  # This is the built-in Django signup form
    success_url = reverse_lazy("login")  # After signing up, go to login page
    template_name = "registration/signup.html"  # Which template to use

from django.shortcuts import render
from .models import Book

def list_books(request):
    """Display all books with their authors"""
    books = Book.objects.all()  # Get all Book records from the database
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Make sure Library is imported

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # this will be used in the template


