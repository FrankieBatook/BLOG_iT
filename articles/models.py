from datetime import date
from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='deafult.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'