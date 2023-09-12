from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def first_name(self) -> str:
        return self.user.first_name
    def last_name(self) -> str:
        return self.user.last_name
    def __str__(self) -> str:
        return self.user.username

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='library/images/artists')
    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    image = models.ImageField(upload_to='library/images/album')
    date_release = models.DateField()
    def __str__(self) -> str:
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title

class Music(models.Model):
    file = models.FileField(upload_to='library/music')
    title = models.CharField(max_length=255)
    artist = models.ManyToManyField(Artist, related_name='musics')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics')
    lyric = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='musics')
    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    discription = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name = 'reviews')
    def __str__(self) -> str:
        return self.profile.user.username
    
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='playlists')
    songs = models.ManyToManyField(Music)

    def __str__(self) -> str:
        return f"{self.name} for {self.profile.user.first_name}"

class LikesPlaylist(models.Model):
    profile = models.OneToOneField(Profile, unique=True, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Music)

    def __str__(self) -> str:
        return f"{self.profile.user.first_name}'s likes"