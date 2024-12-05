from django.db import models
from django.contrib import admin
import os

# Create your models here.
# TODO: specify the image dictionary
game_image_dict = 'games'
series_image_dict = 'series'

class GameSeries(models.Model):
    """
    A game series model.\n
    name, first_release_date, last_release_date, total_number_of_games, genre, developer, image,
    """
    def upload_location(instance, filename):
        filebase, extension = os.path.splitext(filename)
        return f'{series_image_dict}/{instance.name}{extension}'
    
    
    name = models.CharField(max_length=200)
    first_release_date = models.DateField()
    last_release_date = models.DateField()
    total_number_of_games = models.IntegerField()
    genre = models.CharField(max_length=200) # TODO: think about converting to choices
    developer = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.name

class Game(models.Model):
    """
    A game model.\n
    name, image, time_to_beat, release_year, genre, series_id,
    """
    def upload_location(instance, filename):
        filebase, extension = os.path.splitext(filename)
        return f'{game_image_dict}/{instance.name}{extension}'
    

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location)
    release_year = models.IntegerField()
    time_to_beat = models.DecimalField(max_digits=5, decimal_places=2) # up to 999.99
    genre = models.CharField(max_length=200) # TODO: think about converting to choices
    series_id = models.ForeignKey(to=GameSeries, on_delete=models.CASCADE) # TODO: think about standalone games
    
    def __str__(self):
        return self.name
    
    # IGDB API


class User(models.Model):
    """
    A user model.\n
    email, name, password_hash, time_created,
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password_hash = models.CharField(max_length=200)
    time_created = models.DateTimeField()

    def __str__(self):
        return self.name

class UserGame(models.Model):
    """
    A model so user can see his games and their progress.\n
    user_id, game_id, status, started_date, completed_date,
    """
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE) # when user deleted -> UserGame deleted
    game_id = models.ForeignKey(to=Game, on_delete=models.CASCADE) # when game deleted -> UserGame deleted
    status = models.CharField(max_length=200) # TODO: convert to choices
    started_date = models.DateField()
    completed_date = models.DateField()


# TODO: Think about creating a userSeries class so one can see their progress in a series?