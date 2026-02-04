# Django Library API

Una API REST para gestionar una biblioteca digital con autores y libros, construida con Django y Django REST Framework.

## 📋 Descripción

Este proyecto proporciona una API REST para administrar:
- **Autores**: Información de autores con nacionalidad, fecha de nacimiento y biografía
- **Libros**: Catálogo de libros vinculados a autores con ISBN, fecha de publicación y disponibilidad

## 🚀 Tecnologías

- **Django** 6.0.2
- **Django REST Framework** 3.14.0
- **Python** 3.x
- **MySQL** (base de datos)
- **PyMySQL** 1.1.0

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd django-library-api
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el archivo `.env.example` a `.env` y configura tus valores:
```bash
cp .env.example .env
```

Luego edita `.env` con tus credenciales de MySQL:
```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=library_db
DB_USER=root
DB_PASSWORD=tu-contraseña
DB_HOST=localhost
DB_PORT=3306
```

### 5. Aplicar migraciones
```bash
cd library
python manage.py migrate
```

### 6. Crear un superusuario
```bash
python margar datos iniciales (Opcional)

Para cargar autores y libros de ejemplo:
```b8sh
python manage.py shell < load_data.py
```

### 7. Canage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000/`

## 📚 Endpoints API

### Autores
- `GET /api/authors/` - Listar todos los autores
- `POST /api/authors/` - Crear un nuevo autor
- `GET /api/authors/{id}/` - Obtener detalles de un autor
- `PUT /api/authors/{id}/` - Actualizar un autor
- `DELSeguridad y Variables de Entorno

El proyecto utiliza `python-dotenv` para gestionar variables de entorno de forma segura:

- **Archivo `.env`**: Contiene credenciales sensibles (se ignora en Git)
- **Archivo `.env.example`**: Template de referencia para nuevos desarrolladores
- **No subir `.env` al repositorio**: Está en `.gitignore`

**Importante**: Asegúrate de cambiar `SECRET_KEY` en producción:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
- `GET /api/books/` - Listar todos los libros
- `POST /api/books/` - Crear un nuevo libro
- `GET /api/books/{id}/` - Obtener detalles de un libro con información del autor

## 🔐 Autenticación

Todos los endpoints requieren autenticación. Usa las credenciales del superusuario creado para obtener un token.

## 🔐 Seguridad y Variables de Entorno

El proyecto utiliza `python-dotenv` para gestionar variables de entorno de forma segura:

- **Archivo `.env`**: Contiene credenciales sensibles (se ignora en Git)
- **Archivo `.env.example`**: Template de referencia para nuevos desarrolladores
- **No subir `.env` al repositorio**: Está en `.gitignore`

**Importante**: Asegúrate de cambiar `SECRET_KEY` en producción:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 📂 Estructura del Proyecto

```
django-library-api/
├── library/                 # Configuración principal del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py             # URLs principales
│   ├── wsgi.py
│   └── asgi.py
├── books/                  # Aplicación de libros y autores
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas API
│   ├── serializers.py      # Serializadores DRF
│   ├── urls.py             # URLs de la app
│   └── admin.py            # Panel de administración
├── users/                  # Aplicación de usuarios
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── manage.py               # Herramienta de gestión de Django
├── db.sqlite3              # Base de datos (desarrollo)
└── requirements.txt        # Dependencias del proyecto
```

## 🗄️ Modelos de Datos

### Author
- `name` (CharField): Nombre del autor
- `nationality` (CharField): Nacionalidad
- `birth_date` (DateField): Fecha de nacimiento
- `biography` (TextField): Biografía (opcional)

### Book
- `title` (CharField): Título del libro
- `author` (ForeignKey): Referencia al autor
- `isbn` (CharField): ISBN único del libro
- `publication_date` (DateField): Fecha de publicación
- `pages` (IntegerField): Número de páginas
- `available` (BooleanField): Disponibilidad del libro

## 🔧 Desarrollo

### Crear una migración
```bash
python manage.py makemigrations
```

### Ver migraciones pendientes
```bash
python manage.py showmigrations
```

### Panel de administración
Accede a `http://localhost:8000/admin/` con las credenciales del superusuario

## ⚙️ Configuración de Seguridad

Para producción:
1. Cambiar `DEBUG = False` en `settings.py`
2. Cambiar `SECRET_KEY` a una clave segura
3. Agregar los hosts permitidos a `ALLOWED_HOSTS`
4. Usar variables de entorno para credenciales sensibles

## 📝 Licencia

Este proyecto está disponible bajo la licencia MIT.

## 👤 Autor

Ana

## 📧 Contacto

Para preguntas o sugerencias, contacta a través del repositorio.
