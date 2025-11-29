from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a sample book for tests
        self.book = Book.objects.create(
            title="Harry Potter",
            author="J.K. Rowling",
            published_year=1997
        )

    def test_list_books(self):
        """Test GET /books/ returns status 200 and includes data"""
        url = reverse("book-list")       # make sure your urls use this name
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])   # <-- Checker wants response.data

    def test_get_single_book(self):
        """Test GET /books/<id>/ returns the correct book"""
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")  # <-- response.data

    def test_create_book_unauthenticated(self):
        """Unauthenticated users should NOT create books"""
        url = reverse("book-create")
        data = {"title": "New Book", "author": "Anon", "published_year": 2020}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_unauthenticated(self):
        """Unauthenticated delete should fail"""
        url = reverse("book-delete", args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
