# Create Operation

```python
from mybookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)
# Expected Output:
# 1984 by George Orwell (1949)

Save and close.

---

### 📗 2. `retrieve.md`
Now create another file called `retrieve.md` and paste:

```markdown
# Retrieve Operation

```python
books = Book.objects.all()
print(books)
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book = books[0]
print(book.title)
print(book.author)
print(book.publication_year)
# Expected Output:
# 1984
# George Orwell
# 1949

Save and close.

---

### 📙 3. `update.md`
Create `update.md` and paste:

```markdown
# Update Operation

```python
book.title = "Nineteen Eighty-Four"
book.save()

book2 = Book.objects.get(pk=book.pk)
print(book2)
# Expected Output:
# Nineteen Eighty-Four by George Orwell (1949)

Save and close.

---

### 📕 4. `delete.md`
Create `delete.md` and paste:

```markdown
# Delete Operation

```python
result = book2.delete()
print(result)
# Expected Output:
# (1, {'mybookshelf.Book': 1})

print(Book.objects.all())
# Expected Output:
# <QuerySet []>

Save and close.

---

## 🧾 Step 8 — Combine all into one summary file (optional but good practice)

Create another file called `CRUD_operations.md`  
and paste this (it combines all 4 parts neatly):

```markdown
# CRUD Operations in Django Shell

## 1. Create
```python
from mybookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)
# Expected Output: 1984 by George Orwell (1949)
