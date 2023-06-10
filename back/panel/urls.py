from django.urls import path
from .views import auth, main

app_name = 'panel'

urlpatterns = [
   path('sign-in', auth.sign_up, name='sign-in'),
   path('', main.main, name='main'),   
]
