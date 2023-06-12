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

import os
import zipfile

from django.contrib.auth.models import User
from ..models import Profile, Game, GameVersion, GameScore
from ..serializers import (GameSerializer, 
                           GameVersionSerializer, 
                           CreateGameSerializer,
                           GameScoreSerializer)

from ..utils import generate_slug


@api_view(['GET', 'POST'])
def games(request):
   if request.method == 'GET':
      games = Game.objects.all()
      
      return Response({
         'content': GameSerializer(games, many=True).data
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
         
         serializer = CreateGameSerializer(data=data)
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
         }, status=HTTP_403_FORBIDDEN)
         
@api_view(['GET', 'PUT', 'DELETE'])
def game(request, slug):
   try: 
      game = Game.objects.get(slug=slug)
      
      if request.method == 'GET':
         uploadTimestamp = thumbnail = gamePath = ''
         scores_count  = 0
         
         game_version = GameVersion.objects.filter(game=game).last()
         if game_version != None:
            uploadTimestamp = game_version.version
            gamePath = game_version.path_to_game
            thumbnail = f'{game_version.path_to_game}/thumbnail.png'
            game_scores = GameScore.objects.filter(game_version=game_version)
         
         response = {
            'slug': game.slug,
            'title': game.title,
            'description': game.description,
            'author': game.author.username,
            'thumbnail': f'/{thumbnail}',
            'uploadTimestamp': uploadTimestamp,
            'scoreCount': scores_count,
            'gamePath': f'/{gamePath}/index.html',
         }
         
         return Response(response, status=HTTP_200_OK)
         
      if request.user == game.author:
         if request.method == 'PUT':
            title = request.data['title']
            description = request.data['description']
            
            game.title = title
            game.description = description
            game.save()
            
            return Response({
               "status": 'success',
            }, status=HTTP_200_OK)
            
         elif request.method == 'DELETE':
            game.delete()
            
            return Response({}, status=HTTP_204_NO_CONTENT)
      return Response({
         'status': 'forbidden',
         'message': f'You are not the game author',
         } , status=HTTP_403_FORBIDDEN)
         
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)
      
@api_view(['POST'])
def game_upload(request, slug):
   try: 
      game = Game.objects.get(slug=slug)
      user = User.objects.get(id=game.author.id)
      
      game_versions = GameVersion.objects.filter(game=game)
      
      if request.method == 'POST':
         if request.user == game.author:
            zip_file = request.FILES.get('zip')
            
            game_version = GameVersion.objects.create(
               game = game,
               path_to_zip_game = zip_file,
            )         
            
            destination_path = 'static/media/games/zip'
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(destination_path)
                
            game_version.path_to_game = f'{destination_path}/{zip_file.name[:-4]}'
            game_version.save()

            return Response({
               'zip': zip_file.name,
            }, status = HTTP_200_OK)
         
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)
      
@api_view(['GET'])
def game_version(request, slug):
   try: 
      game = Game.objects.get(slug=slug)
      game_version = GameVersion.objects.filter(game=game).last()
      
      if request.method == 'GET':
         path =  f'/{game_version.path_to_game}/index.html'
         
         return Response({
           'path': path,
        }, status=HTTP_200_OK)
        
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)
      
@api_view(['GET', 'POST'])
def scores(request, slug):
   try: 
      game = Game.objects.get(slug=slug)
      game_version = GameVersion.objects.filter(game=game).last()
      game_scores = GameScore.objects.filter(game_version=game_version)
      
      if request.method == 'GET':
         return Response({
           'scores': GameScoreSerializer(game_scores, many=True).data,
        }, status=HTTP_200_OK)
         
      if request.method == 'POST':
         if request.user.is_authenticated:
            scores = request.data['scores']
         
            score = GameScore.objects.create(
               score= scores,
               game_version = game_version,
               user = request.user
            )
            
            return Response({
               "status": "success"
            }, status = HTTP_201_CREATED)
            
         return Response({
         'status': 'forbidden',
         'message': f'You are not the game author',
         } , status=HTTP_403_FORBIDDEN)
        
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)