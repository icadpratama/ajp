from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from datetime import datetime

User = settings.AUTH_USER_MODEL
import re

class EventQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query)
                    )

        return self.filter(lookup)

class EventManager(models.Manager):
    def get_queryset(self):
        return EventQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

# Create your models here.
class Event(models.Model):
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    thumbnail = models.FileField(null=True, blank=False, upload_to='Event/thumbnail/')
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True, default=datetime.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = EventManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = re.sub('[^A-Za-z0-9]+','-',self.title).lower()
        super(Event, self).save()