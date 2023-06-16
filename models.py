from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
class cat(models.Model):
    cat = models.CharField(max_length=225)
    def __str__(self):
        return self.cat
    def get_absolute_url(self):
        return reverse('home')

class post(models.Model):
    title=models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #body = models.TextField()
    body = RichTextField(blank=True,null = True)
    cat = models.CharField(max_length=225,default='coding')
  
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_post')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('show', kwargs={'pk': self.pk})
    def tottallikes(self):
        return self.likes.count()