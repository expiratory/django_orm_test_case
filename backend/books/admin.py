from django.contrib import admin
from .models import Book, Author, BookSale


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BookSale)
class BookSaleAdmin(admin.ModelAdmin):
    raw_id_fields = ('book',)
