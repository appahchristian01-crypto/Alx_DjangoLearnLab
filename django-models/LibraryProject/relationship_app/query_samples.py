# This file is meant to be run inside the Django shell like:
#    python manage.py shell < relationship_app/query_samples.py
#
# It will create some example data and print answers to the requested queries.

# --- Create sample data ---
# Authors and Books
a1 = Author.objects.create(name="Alice")
a2 = Author.objects.create(name="Bob")

b1 = Book.objects.create(title="Alice's Adventures", author=a1)
b2 = Book.objects.create(title="More Adventures of Alice", author=a1)
b3 = Book.objects.create(title="Bob's Big Book", author=a2)

# Libraries and relationships
lib1 = Library.objects.create(name="Central Library")
lib2 = Library.objects.create(name="Eastside Library")

# Add books to libraries (ManyToMany)
lib1.books.add(b1, b3)  # Central has Alice's and Bob's book
lib2.books.add(b2)      # Eastside has the other Alice book

# Librarians (one per library)
l1 = Librarian.objects.create(name="Lola", library=lib1)
l2 = Librarian.objects.create(name="Sam", library=lib2)

print("=== Sample data created ===")

# --- Queries required by the task ---

# 1) Query all books by a specific author (e.g., Alice)
author_name = "Alice"
books_by_alice = Book.objects.filter(author__name=author_name)
print(f"\nBooks by {author_name}:")
for book in books_by_alice:
    print(" -", book.title)

# 2) List all books in a library (e.g., Central Library)
library_name = "Central Library"
try:
    central = Library.objects.get(name=library_name)
    central_books = central.books.all()
    print(f"\nBooks in {library_name}:")
    for book in central_books:
        print(" -", book.title, "(author:", book.author.name + ")")
except Library.DoesNotExist:
    print(f"\nNo library named {library_name} found.")

# 3) Retrieve the librarian for a library (e.g., Eastside Library)
library_name2 = "Eastside Library"
try:
    east = Library.objects.get(name=library_name2)
    print(f"\nLibrarian for {library_name2}: {east.librarian.name}")
except Library.DoesNotExist:
    print(f"\nNo library named {library_name2} found.")
except AttributeError:
    print(f"\nNo librarian assigned to {library_name2}.")
