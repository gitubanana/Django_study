from django.contrib import admin
from .models import Post, PostImage, Comment
import admin_thumbnails


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Post",
            {
                "fields": ["user", "content"],
            }
        ),
    ]
    inlines = [
        CommentInline,
        PostImageInline,
    ]
    list_display = [
        "user",
        "content",
        "created",
    ]
    search_fields = ["content"]
