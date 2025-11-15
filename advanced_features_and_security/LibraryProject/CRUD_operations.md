# CRUD Operations in Django Shell

This document records all Create, Retrieve, Update, and Delete operations performed on the **Book** model in the **mybookshelf** app.

---

## 1️⃣ CREATE

```python
from mybookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)
# Expected Output:
# 1984 by George Orwell (1949)
