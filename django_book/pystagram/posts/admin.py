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


class LikeUserInline(admin.TabularInline):
    model = Post.like_users.through
    verbose_name = "좋아요 한 User"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
        LikeUserInline,
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
