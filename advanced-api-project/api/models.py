from django.db import models

# Author: stores the name of a book author
class Author(models.Model):
    name = models.CharField(max_length=255)  # the author's name

    def __str__(self):
        # Helpful text shown in the admin and shell
        return self.name

# Book: stores a title, year, and which author wrote it
class Book(models.Model):
    title = models.CharField(max_length=255)   # book title
    publication_year = models.IntegerField()   # year the book was published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )  # link the book to an Author (one author -> many books)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
