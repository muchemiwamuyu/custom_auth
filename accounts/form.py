from .models import Profile
from django import forms
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ( 'bio', 'profile_photo', 'contact', 'location')