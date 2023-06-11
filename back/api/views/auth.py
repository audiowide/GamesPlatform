from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_201_CREATED)

from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth.hashers import make_password

from ..validations import validate_email, validate_username
from ..utils import authenticate
from ..models import Profile


#! Sign Up
@api_view(['POST'])
def sign_up(request):
   username = validate_username(request.data['username'])
   email = validate_email(request.data['email'])
   password = request.data['password']
   
   user = User.objects.create(
      username=username,
      email=email,
      password=make_password(password)
   )
   
   refresh = RefreshToken.for_user(user)
   
   refresh_token = str(refresh)
   token = str(refresh.access_token)
   
   return Response({
      'status': 'success',
      'token': token,
      'refresh_token': refresh_token
   }, status=HTTP_201_CREATED)

#! Sign In
@api_view(['POST'])
def sign_in(request):
   email = request.data['email']
   password = request.data['password']
   user = authenticate(email, password)
   
   if user is not None:
      login(request, user)
      
      refresh = RefreshToken.for_user(user)
      
      refresh_token = str(refresh)
      access_token = str(refresh.access_token)
      
      return Response({
         'status': 'success',
         'token': access_token,
         'refresh_token': refresh_token,
         }, status=HTTP_201_CREATED)
   else:
      return Response({'message': 'user not found'}, 
         status=HTTP_401_UNAUTHORIZED)

#! Sign Out
@api_view(['POST'])
def sign_out(request):
   logout(request)
   
   return Response({
      "status": "success"
   }, 200)