from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    SearchResultsView,
)

urlpatterns = [
    # Home – list all posts
    path('', PostListView.as_view(), name='post-list'),

    # Post detail
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Create post
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Edit post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),

    # Delete post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # ⭐ Tag filtering (REQUIRED FOR YOUR TASK)
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # ⭐ Search (REQUIRED FOR YOUR TASK)
    path('search/', SearchResultsView.as_view(), name='search-results'),
]
