from django.contrib import admin
from .models import Profile, Game, GameScore, GameVersion

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(GameScore)
admin.site.register(GameVersion)
