from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import  Profile, Game, GameVersion, GameScore


class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = ('username', 'email', 'last_login', 'date_joined')

class ProfileSerializer(ModelSerializer):
   user = UserSerializer(many=False)
   
   class Meta:
      model = ('id', 'user', 'ava', 'location', 'bio')
   
class GameSerializer(ModelSerializer):
   author = UserSerializer(many=False)
   
   class Meta:
      model = Game
      fields = ('id', 'title', 'slug', 'author', 'description', 'created', 'updated')

class CreateGameSerializer(ModelSerializer):
   class Meta:
      model = Game
      fields = ('id', 'title', 'slug', 'author', 'description', 'created', 'updated')

class GameVersionSerializer(ModelSerializer):
   class Meta:
      model = GameVersion
      fields = ('id', 'game', 'path_to_zip_game' ,'path_to_game', 'version')
      
class GameScoreSerializer(ModelSerializer):
   user = UserSerializer(many=False)
   game_version = GameVersionSerializer(many=False)
   
   class Meta:
      model = GameScore
      fields = ('id', 'user', 'game_version', 'score', 'created', 'updated')
      
class GameAuthoredSerializer(ModelSerializer):
   author = UserSerializer(many=False)
   
   class Meta:
      model = Game
      fields = ('title', 'slug', 'description', 'author')