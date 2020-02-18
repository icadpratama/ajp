from django.db import models
from django.core.validators import validate_email, RegexValidator
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from datetime import datetime

# Create your models here.
class Aspiration(models.Model):
    alphanumeric = RegexValidator(r'^[0-9]*$', 'Only alphanumeric characters are allowed.')

    FIELD_OPTIONS = (
        ('1','Kementerian Pendidikan dan Kebudayaan'),
        ('2','Kementerian Pariwisata dan Ekonomi Kreatif'),
        ('3','Kementerian Pemuda dan Olahraga')
        ('4','Perpustakaan Nasional')
    )

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, validators=[validate_email])
    phone = models.CharField(max_length=13, validators=[alphanumeric])
    title = models.CharField(max_length=60)
    field = models.CharField(max_length=1, choices=FIELD_OPTIONS)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True, default=datetime.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title