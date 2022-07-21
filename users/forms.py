from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# creading a user form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_no = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'password1', 'password2']



