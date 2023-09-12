from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from django.conf import settings
from .models import *
from .serializers import *

class MusicViewSet(ViewSet):
    def list(self, request):
        queryset = Music.objects.select_related('album').all()
        serializer = MusicSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        print(pk)
        queryset = Music.objects.select_related('album').get(pk = pk)
        serializer = MusicSerializer(queryset)
        return Response(serializer.data)
    
    @action(detail=True)
    def add_to_a_playlist(self, request, pk):
        return redirect(f"http://127.0.0.1:8000/library/home/{pk}/add_to_playlist")

class AddToPlaylistViewset(ModelViewSet):
    def get_queryset(self):
        return Playlist.objects.filter(profile__id = self.request.user.id)
    def retrieve(self, request, *args, **kwargs):
        playlist = Playlist.objects.get(id = self.kwargs['pk'])
        playlist.songs.set(self.kwargs['nested_1_pk'])
        playlist.save()
        return redirect(f"http://127.0.0.1:8000/library/my_playlists/{self.kwargs['pk']}/")
    serializer_class = SimplePlaylistSerializer

class AllArtistsViewset (ViewSet):
    def list(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk): # pk is the name of the artist
        print(f"\n\n{pk}")
        queryset = Artist.objects.get(name=pk)
        serializer = ArtistSerializer(queryset)
        print(f"\n\n{serializer.data}\n\n")
        return redirect(f"http://127.0.0.1:8000/library/artist_all_songs/{serializer.data['name']}")

class ArtistAllSongs (ViewSet):
    def list(self, request, name):
        print(f"\n\n\n{self.kwargs}\n\n{request}\n\n{name}\n\n")
        queryset = Music.objects.filter(artist__name=name)
        serializer = ArtistMusicSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self, request, **kwargs):
        queryset = Music.objects.get(id = kwargs['pk'])
        serializer = ArtistMusicSerializer(queryset)
        print(f"this is retrieve\n\n\n{self.kwargs}\n\n{request}\n\n{kwargs}")
        return Response(serializer.data)

class MyPlaylistViewset(ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Playlist.objects.filter(profile__id = self.request.user.id)
        if self.action == 'retrieve':
            print(f"\n\n\n{self.kwargs}")
            return Playlist.objects.filter(id = int(self.kwargs['pk']))
        
    def get_serializer_class(self):
        if len(self.kwargs) == 0:
            return SimplePlaylistSerializer
        elif len(self.kwargs) == 1:
            return PlaylistSerializer

    def get_serializer_context(self):
            return {'profile_id': self.request.user.id}