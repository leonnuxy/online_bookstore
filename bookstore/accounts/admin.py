from django.contrib import admin
from .models import User, Profile, Post, Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'is_member', 'is_active')
    list_filter = ('is_admin', 'is_member', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date', 'image')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ('user',)

admin.site.register(Profile, ProfileAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    list_filter = ('user',)
    search_fields = ('user', 'title')
    ordering = ('user', 'title')

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at')
    list_filter = ('user', 'post')
    search_fields = ('user', 'post', 'content')
    ordering = ('user', 'post', 'content')

admin.site.register(Comment, CommentAdmin)