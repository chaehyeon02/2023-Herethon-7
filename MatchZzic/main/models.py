from django.db import models
from django import forms
from account.models import User

# Create your models here.
class Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    travel_to = models.CharField(verbose_name='여행지', max_length=30, null=True)
    
    def __str__(self):
        return self.travel_to
