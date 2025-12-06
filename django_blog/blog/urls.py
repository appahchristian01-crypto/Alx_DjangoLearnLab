from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,      # <-- REQUIRED
    SearchResultsView,      # <-- REQUIRED
    register,
    profile,
    search,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [

    # -----------------------------
    # Post CRUD
    # -----------------------------
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # -----------------------------
    # ⭐ Tag Filtering (Required)
    # -----------------------------
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # -----------------------------
    # ⭐ Search (Required)
    # -----------------------------
    path('search/', SearchResultsView.as_view(), name='search-results'),

    # -----------------------------
    # User Authentication
    # -----------------------------
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post-list'), name='logout'),

    # -----------------------------
    # Comment CRUD
    # -----------------------------
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-del_
