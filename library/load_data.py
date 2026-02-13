"""
Script para cargar datos iniciales en la aplicación.

Uso: python manage.py shell < load_data.py
"""

from books.models import Author, Book
from datetime import date

# Crear autores si no existen
authors_data = [
    {
        'name': 'Gabriel García Márquez',
        'nationality': 'Colombia',
        'birth_date': date(1927, 3, 6),
        'biography': 'Escritor y periodista colombiano, premio Nobel de Literatura 1982.'
    },
    {
        'name': 'Jorge Luis Borges',
        'nationality': 'Argentina',
        'birth_date': date(1899, 8, 24),
        'biography': 'Escritor argentino, considerado uno de los autores más importantes del siglo XX.'
    },
    {
        'name': 'Isabel Allende',
        'nationality': 'Chile',
        'birth_date': date(1942, 8, 2),
        'biography': 'Novelista chilena, autora de obras de ficción histórica y realismo mágico.'
    }
]

# Crear libros si no existen
books_data = [
    {
        'title': 'Cien años de soledad',
        'author_name': 'Gabriel García Márquez',
        'isbn': '9788401014667',
        'publication_date': date(1967, 5, 30),
        'pages': 417
    },
    {
        'title': 'El amor en los tiempos del cólera',
        'author_name': 'Gabriel García Márquez',
        'isbn': '9788401009385',
        'publication_date': date(1985, 11, 11),
        'pages': 348
    },
    {
        'title': 'Ficciones',
        'author_name': 'Jorge Luis Borges',
        'isbn': '9788430910489',
        'publication_date': date(1944, 8, 15),
        'pages': 256
    },
    {
        'title': 'La casa de los espíritus',
        'author_name': 'Isabel Allende',
        'isbn': '9788401014662',
        'publication_date': date(1982, 10, 5),
        'pages': 368
    },
    {
        'title': 'El coronel no tiene quién le escriba',
        'author_name': 'Gabriel García Márquez',
        'isbn': '9788420650975',
        'publication_date': date(1961, 5, 15),
        'pages': 112
    }
]

# Crear autores
print("Creando autores...")
for author_data in authors_data:
    author, created = Author.objects.get_or_create(
        name=author_data['name'],
        defaults={
            'nationality': author_data['nationality'],
            'birth_date': author_data['birth_date'],
            'biography': author_data['biography']
        }
    )
    if created:
        print(f"✓ Autor creado: {author.name}")
    else:
        print(f"- Autor ya existe: {author.name}")

# Crear libros
print("\nCreando libros...")
for book_data in books_data:
    author = Author.objects.get(name=book_data['author_name'])
    book, created = Book.objects.get_or_create(
        isbn=book_data['isbn'],
        defaults={
            'title': book_data['title'],
            'author': author,
            'publication_date': book_data['publication_date'],
            'pages': book_data['pages'],
            'available': True
        }
    )
    if created:
        print(f"✓ Libro creado: {book.title}")
    else:
        print(f"- Libro ya existe: {book.title}")

print("\n✅ Datos iniciales cargados correctamente!")
