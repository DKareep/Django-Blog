from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100) # 120 chars
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) # able to edit added time auto_now_add


    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title