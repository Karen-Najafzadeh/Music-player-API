from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title','file','album']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['profile','music']

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'profile']

@admin.register(LikesPlaylist)
class LikesPlaylistAdmin(admin.ModelAdmin):
    list_display = ['profile']