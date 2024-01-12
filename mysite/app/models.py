from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Blog(models.Model):
    name=models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name