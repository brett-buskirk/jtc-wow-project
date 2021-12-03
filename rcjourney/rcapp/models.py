from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# TODO add user model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        default='profile1.png', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

# TODO add tag model


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

# TODO add post model


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True,)
    tags = models.ManyToManyField(Tag)
