from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

    
class Image(models.Model):
    photo = models.ImageField(upload_to = "myimage")
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    content = models.TextField(default='hello')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE,default='1')
    favourites = models.ManyToManyField(User,related_name='favourite', default=None, blank=True)

    # def __str__(self):
    #     return self.title