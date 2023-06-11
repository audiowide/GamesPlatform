from django.urls import path
from .views import auth, games

app_name = 'api'

urlpatterns = [
   path('auth/sign-up', auth.sign_up),
   path('auth/sign-in', auth.sign_in),
   path('auth/sign-out', auth.sign_out),
   
]
