from django.urls import path
from .views import auth, main

app_name = 'panel'

urlpatterns = [
   path('sign-in', auth.sign_up, name='sign-in'),
   path('', main.main, name='main'),   
   
   path('games/<int:game_id>', main.game_delete, name='game_delete'),      
]
