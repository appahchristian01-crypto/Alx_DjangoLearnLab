<<<<<<< HEAD
book.title = "Nineteen Eighty-Four"
book.save()

book2 = Book.objects.get(pk=book.pk)
print(book2)
# Expected Output:
# Nineteen Eighty-Four by George Orwell (1949)
=======
book.title = "Nineteen Eighty-Four"
book.save()

book2 = Book.objects.get(pk=book.pk)
print(book2)
# Expected Output:
# Nineteen Eighty-Four by George Orwell (1949)
>>>>>>> b432710 (Add django-models project with relationship_app)
