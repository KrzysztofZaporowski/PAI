from django.contrib import admin
from .models import DatabaseSample

@admin.register(DatabaseSample)
class DatabaseSampleAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'topic', 'size_class')
    search_fields = ('name', 'topic')
    list_filter = ('size_class',)
