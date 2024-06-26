from django.contrib import admin

from .models import Book, Comment


class CommentInlines(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'author', 'price', 'datetime_created', 'datetime_modified')
    inlines = [
        CommentInlines
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'text', 'recommend', 'datetime_created', 'is_active',)
