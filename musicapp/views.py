from django.shortcuts import render
from django.http import HttpResponse
from rest_framework  import viewsets
from .models import Artist, Song, Lyrics
from .serializers import ArtistSerializer, SongSerializer, LyricsSerializer

# Create your views here
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
class LyricsViewSet(viewsets.ModelViewSet):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer
    
    