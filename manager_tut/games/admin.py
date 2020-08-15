from django.contrib import admin

from .models import Game, AgeRating


@admin.register(AgeRating)
class AgeRatingAdmin(admin.ModelAdmin):
    list_display = ("id", "rating")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rating", "release_date", "platform")

