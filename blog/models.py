from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.

class posts(models.Model):
    author = models.CharField(max_length=20)
    slug = models.SlugField(db_index=True, blank=True)
    title = models.CharField(max_length=50)
    author_img = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField(default="")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    post_count = models.IntegerField(default=0)
        
