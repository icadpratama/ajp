# Generated by Django 3.0.3 on 2020-02-09 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='headline',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='news/thumbnail/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=55),
        ),
    ]