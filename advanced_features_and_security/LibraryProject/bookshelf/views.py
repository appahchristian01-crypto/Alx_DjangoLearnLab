from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book


# ---------------------------------------------
# VIEW 1: View list of books  (requires can_view)
# ---------------------------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# ---------------------------------------------
# VIEW 2: Create a book (requires can_create)
# ---------------------------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")

        Book.objects.create(
            title=title,
            author=author,
            description=description
        )
        return redirect('book_list')

    return render(request, 'bookshelf/create_book.html')


# ---------------------------------------------
# VIEW 3: Edit a book (requires can_edit)
# ---------------------------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.description = request.POST.get("description")
        book.save()
        return redirect('book_list')

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# ---------------------------------------------
# VIEW 4: Delete a book (requires can_delete)
# ---------------------------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
