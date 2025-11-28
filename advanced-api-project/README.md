API Views (Django REST Framework)
--------------------------------
We use DRF generic views for Book model:

- GET  /api/books/               -> BookListView (anyone)
- GET  /api/books/<pk>/          -> BookDetailView (anyone)
- POST /api/books/create/        -> BookCreateView (authenticated only)
- PUT  /api/books/<pk>/update/   -> BookUpdateView (authenticated only)
- PATCH /api/books/<pk>/update/  -> BookUpdateView (authenticated only)
- DELETE /api/books/<pk>/delete/ -> BookDeleteView (authenticated only)

Notes:
- BookSerializer enforces that publication_year cannot be in the future.
- Search and ordering available on the list endpoint: ?search=... ?ordering=...
- Use Basic Auth (curl -u username:password) or login through the browsable API to authenticate.
