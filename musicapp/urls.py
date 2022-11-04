from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ArtistViewSet, SongViewSet, LyricsViewSet

router = routers.DefaultRouter()
router.register(r'Artist', views.ArtistViewSet)
router.register(r'Song', views.SongViewSet)
router.register(r'Lyrics', views.LyricsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]
