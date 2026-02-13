from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    total_books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'nationality', 'birth_date', 'biography', 'total_books']

    def get_total_books(self, obj):
        return obj.books.count()
    
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'isbn', 'publication_date', 'pages', 'available']

class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
