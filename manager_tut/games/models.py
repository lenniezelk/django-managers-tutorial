from django.db import models
from django_hint import StandardModelType


class AgeRating(models.Model, StandardModelType):
    rating = models.SmallIntegerField()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"AgeRating({self.pk}): {self.rating}"


class PlatformChoices(models.TextChoices):
    PS4 = "PS4"
    XBOX = "XBOX"


class Game(models.Model, StandardModelType):
    name = models.CharField(max_length=20)
    rating = models.ForeignKey(
        "games.AgeRating", blank=True, null=True, on_delete=models.SET_NULL
    )
    release_date = models.DateField()
    platform = models.CharField(max_length=5, choices=PlatformChoices.choices)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"Game({self.pk}): {self.name}"
