from django.db import models
from django.contrib.auth.models import User

class DatabaseSample(models.Model):
    SIZE_CHOICES = [
        ('small', 'mała'),
        ('medium', 'średnia'),
        ('large', 'duża'),
        ('very_large', 'bardzo duża'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nazwa")
    author = models.CharField(max_length=255, verbose_name="Autorzy")
    topic = models.CharField(max_length=255, verbose_name="Tematyka")
    size_class = models.CharField(max_length=20, choices=SIZE_CHOICES, verbose_name="Klasa wielkości")
    download_link = models.URLField(verbose_name="Link do danych")
    description = models.TextField(max_length=2000, verbose_name="Opis")
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Właściciel")
    complexity = models.PositiveIntegerField(verbose_name="Skomplikowanie (liczba tabel)", null=True, blank=True)
    schema_image = models.ImageField(upload_to='schemas/', null=True, blank=True, verbose_name="Schemat (obraz)")
    ddl_file = models.FileField(upload_to='ddl/', null=True, blank=True, verbose_name="Skrypt DDL")

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Próbka Bazy Danych"
        verbose_name_plural = "Próbki Baz Danych"
        ordering = ['name']

    def __str__(self):
        return self.name

class Question(models.Model):
    database = models.ForeignKey(DatabaseSample, on_delete=models.CASCADE, related_name='questions', verbose_name="Baza danych")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor pytania")
    content = models.TextField(verbose_name="Treść pytania")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pytanie"
        verbose_name_plural = "Pytania"
        ordering = ['-created_at']

    def __str__(self):
        return f"Pytanie od {self.author} do {self.database.name}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name="Pytanie")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor odpowiedzi")
    content = models.TextField(verbose_name="Treść odpowiedzi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Odpowiedź"
        verbose_name_plural = "Odpowiedzi"
        ordering = ['created_at']

    def __str__(self):
        return f"Odpowiedź od {self.author}"

