from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TODO

# Defining Forms Here


class LoginForm(forms.Form):
    '''
    This form is used to login user
    We've utilised constructor for adding bootstrap classes
    '''
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'form-control'})


class SignupForm(UserCreationForm):
    '''
    This form is used to signup user
    We've utilised constructor for adding bootstrap classes
    '''
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'form-control'})


class TODOForm(forms.ModelForm):
    '''
    This form is used to add todo
    We've utilised constructor for adding bootstrap classes
    '''
    class Meta:
        model = TODO
        fields = ['title',  'priority']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'form-control'})
