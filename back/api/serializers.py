from rest_framework.serializers import ModelSerializer, SerializerMethodField

from django.contrib.auth.models import User
from .models import  Profile, Game, GameVersion, GameScore


class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = ('username', 'email', 'last_login', 'date_joined')

class ProfileSerializer(ModelSerializer):
   user = UserSerializer(many=False)
   
   class Meta:
      model = ('id', 'user', 'ava', 'bio')
   
class GameSerializer(ModelSerializer):
    author = UserSerializer(many=False)
    thumbnail = SerializerMethodField()
    scores = SerializerMethodField()

    class Meta:
        model = Game
        fields = ('id', 'title', 'slug', 'author', 'thumbnail', 'description', 'scores', 'created', 'updated')

    def get_thumbnail(self, obj):
        game_version = GameVersion.objects.filter(game=obj).last()
        if game_version is not None:
            return f'/{game_version.path_to_game}/thumbnail.png'
        return ''
   
    def get_scores(self, obj):
      scores_count  = 0
      game_version = GameVersion.objects.filter(game=obj).last()
      if game_version is not None:
         game_scores = GameScore.objects.filter(game_version=game_version)
                  
         if len(game_scores)!= 0:
            for game_score in game_scores:
               scores_count += int(game_score.score)
            return scores_count

         return scores_count
      return scores_count


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
   thumbnail = SerializerMethodField()
   scores = SerializerMethodField()
   
   class Meta:
      model = Game
      fields = ('title', 'slug','thumbnail', 'scores', 'description', 'author')
      
   def get_thumbnail(self, obj):
      game_version = GameVersion.objects.filter(game=obj).last()
      if game_version is not None:
         return f'/{game_version.path_to_game}/thumbnail.png'
      return ''

   def get_scores(self, obj):
      scores_count  = 0
      game_version = GameVersion.objects.filter(game=obj).last()
      if game_version is not None:
         game_scores = GameScore.objects.filter(game_version=game_version)
                  
         if len(game_scores)!= 0:
            for game_score in game_scores:
               scores_count += int(game_score.score)
            return scores_count

         return scores_count
      return scores_count