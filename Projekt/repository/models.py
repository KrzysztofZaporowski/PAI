from django.db import models

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
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Próbka Bazy Danych"
        verbose_name_plural = "Próbki Baz Danych"
        ordering = ['name']

    def __str__(self):
        return self.name
