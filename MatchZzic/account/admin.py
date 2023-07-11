from django.contrib import admin
from .models import User, TempUser

admin.site.register(User)
admin.site.register(TempUser)