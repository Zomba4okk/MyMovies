from .validators import validate_mark
from apps.films.models import Film
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FilmReview(models.Model):
    title = models.CharField(max_length=100)
    mark = models.IntegerField(validators=[validate_mark])
    context = models.TextField(max_length=1000)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='reviews', null=True)
    film = models.ForeignKey(
        to=Film, on_delete=models.CASCADE, related_name='reviews', null=True)