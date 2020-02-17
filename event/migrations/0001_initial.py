# Generated by Django 3.0.3 on 2020-02-17 21:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('subtitle', models.CharField(max_length=120)),
                ('headline', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=60, unique=True)),
                ('thumbnail', models.FileField(null=True, upload_to='Event/thumbnail/')),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
    ]
