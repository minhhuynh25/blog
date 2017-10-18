from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    context = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title