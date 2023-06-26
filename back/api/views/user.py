from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND)

from django.contrib.auth.models import User

from ..models import Profile, Game, GameVersion, GameScore
from ..serializers import GameAuthoredSerializer, GameScoreSerializer

@api_view(['GET', 'PUT'])
def user(request, username):
   try:
      user = User.objects.get(username=username)
      profile = Profile.objects.get(user=user)
      
      if request.method == 'GET':
         games = Game.objects.filter(author=user)
         game_scores = GameScore.objects.filter(user=user)
         
         return Response({
            'username': user.username,
            'ava': f'/static/media/{str(profile.ava)}',
            'bio': profile.bio,
            'registeredTimestamp': user.date_joined,
            'authoredGames': GameAuthoredSerializer(games, many=True).data,
            'highscores': GameScoreSerializer(game_scores, many=True).data
         }, status=HTTP_200_OK)
      
      if request.method == 'PUT':
         if request.user == user:
            image = request.FILES.get('ava')
            bio = request.data.get('bio')
            
            profile.ava = image
            profile.bio = bio
            profile.save()
            
            return Response({
               'status': 'success'
            }, status=HTTP_200_OK)
         
   except:
      return Response({
         "status": "not-found",
         "message": "Not found"
      }, status=HTTP_404_NOT_FOUND)