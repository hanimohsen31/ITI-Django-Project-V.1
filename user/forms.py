from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email','password1','password2']


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name']

class Profileform(forms.ModelForm):
    class  Meta:
        model= Profile
        fields=['phone','image','facebook_profile','country']

