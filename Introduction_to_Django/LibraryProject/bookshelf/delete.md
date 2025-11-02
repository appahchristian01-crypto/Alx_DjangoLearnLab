result = book2.delete()
print(result)
# Expected Output:
# (1, {'mybookshelf.Book': 1})

print(Book.objects.all())
# Expected Output:
# <QuerySet []>

This file serves as your single record of all commands and results for submission.

---

## 🧠 Step 9 — Verify migrations and database are clean

Before submitting, make sure everything is up-to-date.

Run these in your terminal:

```bash
python manage.py makemigrations mybookshelf
python manage.py migrate
python manage.py check
