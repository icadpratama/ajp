from django.db import models
from django.core.validators import validate_email, RegexValidator

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