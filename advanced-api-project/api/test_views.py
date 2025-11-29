from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # create user
        self.user = User.objects.create_user(username="testuser", password="pass123")

        # create sample books
        self.book1 = Book.objects.create(
            title="Harry Potter",
            author="J.K. Rowling",
            published_year=1997
        )
        self.book2 = Book.objects.create(
            title="Narnia",
            author="C.S. Lewis",
            published_year=1950
        )

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_requires_login(self):
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": "Someone",
            "published_year": 2024
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_success(self):
        self.client.login(username="testuser", password="pass123")
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": "Someone",
            "published_year": 2024
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_requires_login(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_success(self):
        self.client.login(username="testuser", password="pass123")
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Book"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        self.client.login(username="testuser", password="pass123")
        url = reverse("book-delete", args=[this.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
