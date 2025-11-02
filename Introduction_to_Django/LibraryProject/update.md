book.title = "Nineteen Eighty-Four"
book.save()

book2 = Book.objects.get(pk=book.pk)
print(book2)
# Expected Output:
# Nineteen Eighty-Four by George Orwell (1949)
