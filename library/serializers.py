from .models import *
from django.conf import settings
from djoser.serializers import UserSerializer as US
from rest_framework import serializers 

#for showing all the users to the admin
# class UserSerializer(serializers.ModelSerializer):
#     class Meta(US.Meta):
#         fields = ['username','first_name','last_name','email']

# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True, many=True)
#     class Meta:
#         model = Profile
#         fields = ['user']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [ 'name', 'image']
        read_only_fields = ['name', 'image']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title']

class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True,read_only=True)
    # genre = GenreSerializer(many=True,read_only=True)
    album = AlbumSerializer(read_only=True)
    class Meta:
        model = Music
        fields = ['id','title', 'file', 'album', 'artist']#, 'genre']
        read_only_fields =  ['id','title', 'file', 'album', 'artist', 'genre']


class ArtistMusicSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    genre = GenreSerializer(many=True,read_only=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'file', 'album', 'genre']

class SimpleArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model =Artist
        fields = ['id', 'name']

class SimplePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name','profile']

class SimpleMusicSerializer(serializers.ModelSerializer):
    artist = SimpleArtistSerializer(many=True,read_only=True)
    class Meta:
        model = Music
        fields = ['id','title','artist']

class SimplePlaylistSerializer(serializers.ModelSerializer):
    # songs = SimpleMusicSerializer(many=True,read_only=False)
    class Meta:
        model = Playlist
        fields = ['id', 'name']

    def create(self, validated_data):
        profile = self.context['profile_id']
        return Playlist.objects.create(profile_id=profile, **validated_data)
    
class PlaylistSerializer(serializers.ModelSerializer):
    songs = MusicSerializer(many=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']