from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_404_NOT_FOUND)
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from ..models import Profile, Game, GameVersion, GameScore
from ..serializers import GameSerializer, GameVersionSerializer 

from ..utils import generate_slug


@api_view(['GET', 'POST'])
def games(request):
   if request.method == 'GET':
      games = Game.objects.all()
      
      return Response({
         'content': games
   }, status=HTTP_200_OK)
   if request.method == 'POST':
      if request.user.is_authenticated:
         title = request.data['title']
         description = request.data['description']
         
         slug = generate_slug(title)

         if slug[0] == 'invalid':
            return Response({
               'status': slug[0],
               'slug': slug[1],
            }, status = HTTP_400_BAD_REQUEST)
         
         data = {
            'title': title,
            'slug': slug[1],
            'author': request.user.id,
            'description': description
         }
         
         serializer = GameSerializer(data=data)
         serializer.is_valid(raise_exception=True)
         game = serializer.save()
         
         return Response({
            'status': 'success',
            'slug': game.slug
         }, status=HTTP_201_CREATED)
      else:
         return Response({
            'status': 'forbidden',
            'message': 'You are not the game author',
         }, status=HTTP_201_CREATED)
         
@api_view(['GET', 'PUT', 'DELETE'])
def game(request, slug):
   try: 
      game = Game.objects.get(slug=slug)
      user = User.objects.get(id=game.id)
      
      if request.method == 'GET':
         scores_count  = 0
         
         response = {
            'slug': game.slug,
            'title': game.title,
            'description': game.description,
            'author': user.username,
            'thumbnail': game.thumbnail,
            'scoreCount': scores_count,
         }
         
         game_version = GameVersion.objects.filter(game=game).last()
         if game_version != None:
            game_scores = GameScore.objects.filter(game_version=game_version)
            
            response += {
               'uploadTimestamp': game_version.version,
               'gamePath': game_version.path_to_game
            }
            
         
         return Response(response, status=HTTP_200_OK)
         
         if request.method == 'PUT':
            title = request.data['title']
            description = request.data['description']
            
            game.title = title
            game.description = description
            game.save()
            
            return Response({
               'status': 'success',
            }, status=HTTP_200_OK)
            
         if request.method == 'DELETE':
            game.delete()
            return Response({}, status=HTTP_204_NO_CONTENT)
         
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)
      
@api_view(['POST'])
def game_upload(request, slug):
   try: 
      game = Game.objects.get(slug=slug)
      user = User.objects.get(id=game.id)
      
      if request.method == 'POST':
         zip = request.data['zip']
         
         return Response({
            'zip': zip,
         }, status = HTTP_200_OK)
         
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)
      
@api_view(['GET'])
def game_version(request, slug, version):
   try: 
      game = Game.objects.get(slug=slug)
      game_version = GameVersion.objects.filter(game=game).last()
      
      if request.method == 'GET':
        return Response({
           'path': game_version.path_to_game
        }, status=HTTP_200_OK)
        
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)