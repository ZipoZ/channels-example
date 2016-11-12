from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import settings

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    def __unicode__(self):
        return self.label

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}

class Topic(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.title

class User(AbstractUser):
    language = models.CharField(max_length=255, choices=settings.LANGUAGE_CHOICES)
    topics_pro = models.ManyToManyField(Topic, related_name='pro')
    topics_against = models.ManyToManyField(Topic, related_name='against')
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username