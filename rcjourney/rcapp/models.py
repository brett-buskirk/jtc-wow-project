from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# TODO add user model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

# TODO add comment model
