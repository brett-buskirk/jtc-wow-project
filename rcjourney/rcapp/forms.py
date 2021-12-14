from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from taggit.forms import TagField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post', 'tags']


class PostForm(forms.Form):
    post = forms.CharField(widget=forms.Textarea, required=True)
    #tag = forms.CharField(widget=forms.CharField)
    # choices = []
    # for tag in Tag.objects.all():
    #     choices.append((tag.tag_id, tag.name))
    # tags = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple, choices=choices, required=True)
    tags = TagField(label="Tags")
