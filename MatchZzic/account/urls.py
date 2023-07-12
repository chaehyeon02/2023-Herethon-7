from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.first, name="first"),
    path('signup/', views.signup, name="signup"),
    path('signup2/', views.signup2, name="signup2"),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('mypage/', views.mypage, name="mypage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)