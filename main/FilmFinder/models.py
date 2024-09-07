from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Film(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    studio = models.CharField(max_length=30)
    score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.name


class User(models.Model):
    mail = models.EmailField(max_length=30)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.mail