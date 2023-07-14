from django.urls import path
from . import views

urlpatterns = [
    path('', views.match, name='match'),
    path('done', views.done, name='finish')
]