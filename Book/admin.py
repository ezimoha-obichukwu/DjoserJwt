from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author"]