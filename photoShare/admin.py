from django.contrib import admin
from .models import Album, AlbumAdmin, Tag, TagAdmin, Image, ImageAdmin

# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
