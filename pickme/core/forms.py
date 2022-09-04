from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    
    # custom user model
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class CustomUserChangeForm(UserChangeForm):
    
    # custom user model
    class Meta:
        model = User
        fields = ('username', 'email')