from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    # Profiles are linked to the native User object in Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Set default profile image for new users
    profile_image = models.ImageField(default='profile1.png', null=True, blank=True)
    # Create field for users to create a bio
    bio = models.TextField(null=True, blank=True)


class Tag(models.Model):
    # Create tags to add to posts
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Post(models.Model):
    # Link posts to the user that created them
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.TextField(blank=True, null=True)
    # Timestamp the post
    date_created = models.DateTimeField(auto_now=True, null=True,)
    # Link the tags to the post and vice versa
    tags = models.ManyToManyField(Tag)
