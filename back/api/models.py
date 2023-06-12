from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ava = models.ImageField(upload_to='avatars', default='ava.jpg')
   location = models.CharField(max_length=200, blank=True)
   bio = models.TextField(max_length=500, blank=True)
   
   isBlocked = models.BooleanField(default=False)
   isBlocked_message = models.CharField(max_length=100, blank=True)
   
   def __str__(self):
      return self.user.username
   
class Game(models.Model):
   title = models.CharField(max_length=255)
   slug = models.CharField(max_length=255, unique=True)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   description = models.TextField(max_length=255, blank=True)
   
   is_deleted  = models.BooleanField(default=False)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.slug
   
class GameVersion(models.Model):
   game = models.ForeignKey(Game, on_delete=models.CASCADE)
   path_to_zip_game = models.FileField(upload_to='games/zip')
   path_to_game = models.CharField(max_length=1000, blank=True)
   version = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.game.slug
   
class GameScore(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   game_version = models.ForeignKey(GameVersion, on_delete=models.CASCADE)
   score = models.IntegerField(default=0)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return '{} - {} - {}'.format(self.user.username, self.game.slug, self.score)