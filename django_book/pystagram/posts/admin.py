from django.contrib import admin
from .models import Post, PostImage, Comment, HashTag
import admin_thumbnails
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
        CommentInline,
    ]
    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }
    list_display = [
        "user",
        "content",
        "created",
    ]
    search_fields = ["content"]


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
