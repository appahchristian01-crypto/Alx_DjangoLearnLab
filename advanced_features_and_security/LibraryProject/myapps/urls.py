from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/create/', views.create_article, name='article_create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
]
