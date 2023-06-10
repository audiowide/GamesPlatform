from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='panel/sign-in')
def main(request):
   if request.user.is_superuser:
      users = User.objects.filter(is_superuser=False)
      admins = User.objects.filter(is_superuser=True)
      
      
      context = {
         'users': users,
         'admins': admins,
      }
      return render(request, 'panel/home.html', context)