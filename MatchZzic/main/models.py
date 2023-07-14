from django.db import models
from django import forms
from account.models import User

# Create your models here.
class Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    place = models.TextField('동행할 여행지', max_length=30, default='')
    
    def __str__(self):
        return self.place