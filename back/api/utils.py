from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from api.models import Game  

import random

# user authentication for sign in
def authenticate(email, password):
   try:
      user = User.objects.get(email=email)
      
      if check_password(password, user.password):
         return user
      return None
   except:
      return None
   
def generate_slug(title):
   slug = "-".join(title.lower().split(' '))
   try:
      game = Game.objects.find(slug=slug)

      return ['invalid', 'Game title already exists']
   except:
      return ['success', slug]