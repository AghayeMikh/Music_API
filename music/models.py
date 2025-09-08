from django.contrib.auth.models import User
from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.artist}"

