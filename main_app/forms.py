from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import User, Movie
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username',
                  'email', 'password1', 'password2', 'gender', 'age']


class MovieForm(forms.ModelForm):
    release_date = forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'
               }),
    movie_title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title'}))

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('posted',)
        widgets = {
            'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here', 'rows': '4', 'cols': '10'}),
            'release_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

        def __init__(self, *args, **kwargs):
            super(MovieForm, self).__init__(*args, **kwargs)
            self.fields['genre'].empty_label = "Select Genre"
