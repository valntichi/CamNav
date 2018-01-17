from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


# business, sports, fashion, etc
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    breaking = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title + " --- " + self.content


class MyTable(models.Model):
    item = models.CharField(max_length=200)
    class Meta:
        db_table = "my_table"


class Photo(models.Model):
    article = models.ForeignKey(Article, related_name='article_img')
    image = models.ImageField(upload_to="/uploads/")
    description = models.CharField(max_length=100, blank=True)


class Advert(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

