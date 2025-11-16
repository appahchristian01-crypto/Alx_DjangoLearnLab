from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        permissions = [
            ("can_create", "Can create a book"),
            ("can_delete", "Can delete a book"),
            ("can_edit", "Can edit a book"),
            ("can_view", "Can view a book"),
        ]

    def __str__(self):
        return self.title
