from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class BlogPost(models.Model):
    blog_postid = models.AutoField(primary_key=True)
    userid = models.AutoField(ForeignKey=True)
    blog_post = models.CharField(max_length=255)

    # ! might want to include comment id in case we want to pull up all blog posts with that have comments with a certain keyword


class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    blog_postid = models.AutoField(ForeignKey=True)
    userid = models.AutoField(ForeignKey=True)
    comment_body = models.CharField(max_length=255)
