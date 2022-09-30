from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads",default = '', blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    visibility = models.CharField(max_length=100,null=True)
    last_updated = models.DateTimeField(auto_now=True)

