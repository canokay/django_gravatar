from django import forms
from django.forms import Form, TextInput, PasswordInput, CharField


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={'class': 'form-control','placeholder':'Kullanıcı Adı','style':'margin-bottom:20px;'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Parola', 'name': 'password', 'id': 'password', 'required': 'required', 'autofocus': 'autofocus', 'data-eye': 'data-eye'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")