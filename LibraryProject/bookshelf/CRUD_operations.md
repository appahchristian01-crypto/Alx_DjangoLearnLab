# Create
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output: <Book: 1984 by George Orwell (1949)>

# Retrieve
>>> Book.objects.all()
# Expected output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
>>> b = Book.objects.first()
>>> b.title, b.author, b.publication_year
# Expected output: ('1984', 'George Orwell', 1949)

# Update
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
# Expected output: (no text) ; object updated
>>> Book.objects.first()
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

# Delete
>>> b.delete()
# Expected output: (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# Expected output: <QuerySet []>
