from django.db import models

# Create your models here.

# TODO add user model


class User(models.Model):
    id = models.AutoField(primary_key=True),
    username = models.CharField(max_length=255),
    email = models.EmailField(max_length=255),
    password = models.CharField(max_length=255),
    first_name = models.CharField(max_length=255, null=True, blank=True),
    last_name = models.CharField(max_length=255, null=True, blank=True),
    profile_image = models.ImageField(null=True, blank=True),
    bio = models.TextField(null=True, blank=True)

# TODO add post model


class Post(models.Model):
    post_id = models.AutoField(primary_key=True),
    user_id = models.ForeignKey('User', on_delete=models.CASCADE),
    post_content = models.TextField(blank=True, null=True),
    date_created = models.DateTimeField(auto_now=True, null=True,)
