from django.db import models
from accounts.models import Profile
from django.core.validators import FileExtensionValidator
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(Profile,blank=True,related_name='likes')
    image = models.ImageField(upload_to='posts',blank=True,validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    def __str__(self):
        return str(self.description[:20])