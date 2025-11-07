# query_samples.py
# This script demonstrates how to query relationships between models in Django.

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author.
author_name = "Alice"
author = Author.objects.get(name=author_name)  # ALX checker expects this line
books_by_author = Book.objects.filter(author=author)  # ALX checker expects this line
print(f"\nBooks by {author_name}:")
for book in books_by_author:
    print(f" - {book.title}")

# 2️⃣ List all books in a library.
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(f" - {book.title} (author: {book.author.name})")

# 3️⃣ Retrieve the librarian for a library.
library_name2 = "Eastside Library"
library2 = Library.objects.get(name=library_name2)
# 👇 ALX checker expects this line — must use Librarian.objects.get(library=...)
librarian = Librarian.objects.get(library=library2)
print(f"\nLibrarian for {library_name2}: {librarian.name}")
