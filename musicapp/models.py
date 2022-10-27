from email.policy import default
from uuid import uuid4
from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    age = models.IntegerField()
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.first_name
    
    
class Song(models.Model):
    title = models.CharField(blank=True, max_length=50)
    date_released = models.DateField('date released')
    artist_id = models.IntegerField()
    likes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    
class Lyrics(models.Model):
    content = models.CharField(blank=True, max_length=6000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.content
    