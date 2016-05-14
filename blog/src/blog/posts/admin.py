from django.contrib import admin

# Register your models here.

from .models import Post #same app hence .model

class PostAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title"]
    search_fields = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

