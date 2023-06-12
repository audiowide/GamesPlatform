from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from api.models import Game

@login_required(login_url='panel/sign-in')
def main(request):
   if request.user.is_superuser:
      users = User.objects.filter(is_superuser=False)
      admins = User.objects.filter(is_superuser=True)
      games = Game.objects.all()
      
      if request.method == 'POST':
         isBlocked = request.POST.get('isBlocked')
         isBlockedMessage = request.POST.get('isBlockedMessage')
         isUserId = request.POST.get('isUserId')
         
         user = User.objects.get(id=isUserId)
         profile = Profile.objects.get(user = user)
         
         block_type = isBlocked
         
         if block_type:
            block_type = False
         else:
            block_type = True
         
         profile.isBlocked = block_type
         profile.isBlocked_message = isBlockedMessage
         
         return redirect('/panel')
      
      context = {
         'users': users,
         'admins': admins,
         'games': games
      }
      return render(request, 'panel/home.html', context)
   
@login_required(login_url='panel/sign-in')
def game_delete(request, game_id):
   if request.user.is_superuser:
      game = Game.objects.get(id=game_id)
      
      game.delete()
      return redirect('/panel')
