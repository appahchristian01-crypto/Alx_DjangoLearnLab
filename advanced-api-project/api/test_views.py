from django.test import TestCase
from .models import Book, Author

class TestBookAPI(TestCase):  # ✅ Class starts with 'Test'
    def setUp(self):
        self.author1 = Author.objects.create(name="Author A")
        self.book1 = Book.objects.create(
            title="Book A",
            published_year=2020,  # use 'published_year', not 'publication_year'
            author=self.author1
        )

    def test_create_book(self):
        self.assertEqual(self.book1.title, "Book A")
