from django.contrib import admin
from .models import *

# Register your models here.
### Admin

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "images", "public"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "title", "user", "rating", "size", "tags_", "albums_", "thumbnail_",
                    "created"]
    list_filter = ["tags", "albums", "user"]

    def save_model(self, request, obj, form, change):
        if not obj.user: obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
