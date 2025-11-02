books = Book.objects.all()
print(books)
# Expected Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book = books[0]
print(book.title)
print(book.author)
print(book.publication_year)
# Expected Output:
# 1984
# George Orwell
# 1949
