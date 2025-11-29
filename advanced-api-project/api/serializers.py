from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer: turns Book objects into data and checks rules
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    # Custom validation: publication_year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer: includes author's name and a nested list of their books
class AuthorSerializer(serializers.ModelSerializer):
    # nested (read-only) list of books — uses our BookSerializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
