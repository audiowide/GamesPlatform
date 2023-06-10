from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# login
def sign_up(request):
   
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
            
      try:
         user = User.objects.get(username=username)
      except:
         messages.error(request, 'User not found')
   
      user = authenticate(username=username, password=password)
      
      print('_____________', user)

      if user is not None:
         if user.is_superuser:
            login(request, user)
            return redirect('panel:main')
         else:
            messages.error(request, 'Invalid password or username')
      else:
         messages.error(request, 'Invalid password or username')
         
   return render(request, 'panel/auth.html')