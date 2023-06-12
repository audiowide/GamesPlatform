from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from api.models import Game  
from rest_framework.pagination import PageNumberPagination

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
   
def paginate_data(request, queryset, serializer):
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Specify the number of items per page

    # Paginate the queryset
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    # Serialize the paginated queryset
    serialized_data = serializer(paginated_queryset, many=True)

    # Return the paginated response
    return paginator.get_paginated_response(serialized_data.data)