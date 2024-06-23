from django.contrib import admin

from .models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'datetime_created', 'datetime_modified')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'text', 'recommend', 'datetime_created', 'is_active',)
