from django.db import models
from django.contrib.auth.models import User
from .utils import getRandom
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    firstName = models.CharField(max_length=200, blank=True)
    lastName = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(default="no bio ...",max_length=400)
    email = models.EmailField(max_length=200,blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="avatar")
    friends=models.ManyToManyField(User, blank=True, related_name="friends")
    slug = models.SlugField(unique=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"

    def save(self,*args, **kwargs):
        ex=False
        if self.firstName and self.lastName:
            
            to_slug = slugify(str(self.firstName)+""+str(self.lastName))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug+""+str(getRandom()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug=str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)
    
    def getAllFriends(self):
        return None if self.friends.all().count()==0 else self.friends.all()
    
    def getCountFriends(self):
        return 0 if self.friends.all().count()==0 else self.friends.all().count()

statusChoice =(('send','send'),('Accepted','Accepted'))
class Relationship(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status=models.CharField(max_length=8,choices=statusChoice)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"