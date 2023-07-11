from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name="first"),
    path('signup/', views.signup, name="signup"),
    path('signup2/', views.signup2, name="signup2"),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),
]