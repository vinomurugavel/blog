from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    blog_title=models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    notion_link=models.CharField(max_length=1000000,null=True)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    thumbnail=models.ImageField(upload_to='thumbanils/')
    