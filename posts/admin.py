from django.contrib import admin
from posts.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','rate','author','category')
    list_filter = ('rate', 'category')

admin.site.register(Category)
admin.site.register(Tag)