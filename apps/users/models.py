from enum import unique
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length=255,unique=True
        )

    def __str__(self):
        return self.username

class Film(models.Model):
    title = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.title

class UserMovie(models.Model):
    user= models.ForeignKey(User,related_name='user_movie',on_delete=models.CASCADE)
    movie = models.ForeignKey(Film,related_name='user_movie',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user','movie')

    def __str__(self):
        return "%s %s" % (self.movie, self.user)