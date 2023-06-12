from django.urls import path
from .views import auth, games, user

app_name = 'api'

urlpatterns = [
   path('auth/sign-up', auth.sign_up),
   path('auth/sign-in', auth.sign_in),
   path('auth/sign-out', auth.sign_out),
   
   path('users/<str:username>', user.user),

   path('games', games.games),
   path('games/<str:slug>', games.game),
   path('games/<str:slug>/game_upload', games.game_upload),
   path('games/<str:slug>/last-version', games.game_version),
   
   path('games/<str:slug>/scores', games.scores),
   
]
