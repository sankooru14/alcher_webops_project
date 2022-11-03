# Generated by Django 4.0.6 on 2022-08-16 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]