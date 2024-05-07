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
    
class Comments(models.Model):
    user=models.ForeignKey(Profile,on_delete = models.CASCADE)
    post=models.ForeignKey(Post,on_delete = models.CASCADE)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.pk)
    

choiceLike = (('Like','Like'),('Unlike','Unlike'))
class Like(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.Case)
    value = models.CharField(choices=choiceLike, max_length=8)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'{self.user} - {self.post} - {self.value}'