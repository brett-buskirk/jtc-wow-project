from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


# User Form for creating new users
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Edit Profile Form for allowing a user to edit their profile
class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


# Post Form for users to post content in the Forum
class PostForm(forms.Form):
    post = forms.CharField(widget=forms.Textarea, required=True)
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=False)
