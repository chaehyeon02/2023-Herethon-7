from django.db import models
from django import forms

# Create your models here.
class Post (models.Model):
    place = models.TextField('동행할 여행지', max_length=30, default='')
    
    def __str__(self):
        return self.place