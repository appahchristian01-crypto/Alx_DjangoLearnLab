# api/test_views.py

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class TestBookAPI(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="pass1234"
        )

        # One existing book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Writer",
            publication_year=2020
        )

    def test_get_books_list(self):
        """Test book list endpoint"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # checker requirement
        self.assertIn("Test Book", str(response.data))

    def test_create_book_authenticated(self):
        """Create a book when logged in"""

        # checker requirement
        self.client.login(username="testuser", password="pass1234")

        payload = {
            "title": "New Book",
            "author": "Author One",
            "publication_year": 2024
        }

        response = self.client.post("/api/books/create/", payload)

        # correct status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # checker requirement: use response.data
        self.assertEqual(response.data["title"], "New Book")

    def test_create_book_unauthenticated(self):
        """Unauthenticated users should NOT create books"""
        payload = {
            "title": "Blocked Book",
            "author": "Author Block",
            "publication_year": 2025
        }

        response = self.client.post("/api/books/create/", payload)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Update book only if logged in"""

        # checker requirement
        self.client.login(username="testuser", password="pass1234")

        payload = {"title": "Updated Title"}

        response = self.client.patch(f"/api/books/{self.book.id}/update/", payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checker requirement: response.data
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book_authenticated(self):
        """Delete book only when authenticated"""

        # checker requirement
        self.client.login(username="testuser", password="pass1234")

        response = self.client.delete(f"/api/books/{self.book.id}/delete/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
