from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])


class CustomLoginForm(AuthenticationForm):
    username = CharField(max_length=255)
    password = CharField()
