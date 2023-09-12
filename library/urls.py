from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nrouter
from . import views    

router = routers.DefaultRouter()
router.register('home', views.MusicViewSet, basename='home') # shows all the musics
router.register('artists', views.AllArtistsViewset,basename='aetists') # shows all the artists
router.register('my_playlists', views.MyPlaylistViewset, basename='playlists') # shows all the user's playlists

add_router = nrouter.NestedDefaultRouter(router, 'home')
add_router.register('add_to_playlist', views.AddToPlaylistViewset, basename='add')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(add_router.urls)),
    path('artist_all_songs/<str:name>', views.ArtistAllSongs.as_view({'get':'list'})),
    path('artist_all_songs/<str:name>/<int:pk>', views.ArtistAllSongs.as_view({'get':'retrieve'}))
]
