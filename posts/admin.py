from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "update", "timestamp"]
    list_display_links = ["update"]
    list_editable = ["title"]
    list_filter = ["update", "timestamp"]
    search_fields = ["title", "context"]
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)