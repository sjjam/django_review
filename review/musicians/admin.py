from django.contrib import admin
from .models import Musician, Album

# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
admin.site.register(Musician, MusicianAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('musician', 'title', 'featuring', 'music_num', 'release_date')
admin.site.register(Album, AlbumAdmin)