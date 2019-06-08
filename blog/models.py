from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import string, random
from django.db.models.query import QuerySet

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)
    subject = models.ForeignKey(Subject, related_name="topics", on_delete=models.CASCADE)





class Post(models.Model):

    
    slug = models.SlugField(max_length=30, unique=True)
    postName = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    topic = models.ForeignKey(Topic, related_name="post", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="post", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.postName

    def __unicode__(self):
        return self.postName




