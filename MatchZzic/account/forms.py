from django import forms
from .models import User, TempUser

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class TempUserForm(forms.ModelForm):
    class Meta:
        model = TempUser
        fields = '__all__'


