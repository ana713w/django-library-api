from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural= "Authors"
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Books"
        ordering = ['-publication_date']  # Most recent first
    
    def __str__(self):
        return f"{self.title} - {self.author.name}"
