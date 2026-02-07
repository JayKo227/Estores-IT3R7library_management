from django.contrib import admin
from .models import Library, Author, Book, Member


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['library_id']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'author_name', 'phone_number', 'gender', 'date_birth_year']
    search_fields = ['author_name']
    list_filter = ['gender']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'book_name', 'author', 'library', 'date_published']
    search_fields = ['book_name']
    list_filter = ['library', 'date_published']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'member_name', 'phone_number', 'gender', 'birth_year', 'book']
    search_fields = ['member_name']
    list_filter = ['gender']
