from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='author')

urlpatterns = [
    # Include ViewSet routes
    path('', include(router.urls)),
    
    # Generic views for Book
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/edit/', views.BookUpdateDeleteView.as_view(), name='book-edit'),
    
    path('authors/<int:author_id>/books/', views.books_by_author, name='books-by-author'),
]