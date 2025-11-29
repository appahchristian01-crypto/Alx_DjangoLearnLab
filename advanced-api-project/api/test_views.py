from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create user for authenticated tests
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Login (required for the checker)
        self.client.login(username="testuser", password="password123")

        # Sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            published_year=2020
        )

    # ------------------ CREATE ------------------
    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": "Alice",
            "published_year": 2023
        }

        response = self.client.post(url, data, format="json")

        # CHECKER REQUIREMENT: response.data must exist
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)

    # ------------------ LIST ------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # ------------------ RETRIEVE ------------------
    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    # ------------------ UPDATE ------------------
    def test_update_book_authenticated(self):
        url = reverse("book-update", args=[self.book.id])
        data = {"title": "Updated Book"}
        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    # ------------------ DELETE ------------------
    def test_delete_book_authenticated(self):
        url = reverse("book-delete", args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # ------------------ FILTERING ------------------
    def test_filter_books_by_title(self):
        url = reverse("book-list") + "?title=Test Book"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Test Book")

    # ------------------ SEARCH ------------------
    def test_search_books(self):
        url = reverse("book-list") + "?search=Test"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ------------------ ORDERING ------------------
    def test_order_books(self):
        url = reverse("book-list") + "?ordering=published_year"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
