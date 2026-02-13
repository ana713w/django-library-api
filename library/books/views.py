from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, BookDetailSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return Response(
                {"error": "Only administrators can delete authors"},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
    

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/
    Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/{id}/
    Retrieve a specific book with full author details.
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/books/{id}/edit/
    PUT /api/books/{id}/edit/
    DELETE /api/books/{id}/edit/
    
    Update or delete a book.
    Only admins can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        """
        Only admin users can delete books.
        """
        if not request.user.is_staff:
            return Response(
                {"error": "Only administrators can delete books"},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def books_by_author(request, author_id):
    """
    GET /api/authors/{author_id}/books/
    """
    try:
        author = Author.objects.get(id=author_id)
        books = author.books.all()
        
        # Calculate statistics
        total_pages = sum([book.pages for book in books])
        
        data = {
            'author': AuthorSerializer(author).data,
            'statistics': {
                'total_books': books.count(),
                'available_books': books.filter(available=True).count(),
                'unavailable_books': books.filter(available=False).count(),
                'total_pages': total_pages,
                'average_pages': total_pages // books.count() if books.count() > 0 else 0,
            },
            'books': BookSerializer(books, many=True).data
        }
        
        return Response(data)
        
    except Author.DoesNotExist:
        return Response(
            {'error': 'Author not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )