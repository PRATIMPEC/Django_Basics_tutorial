from django.db import models

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Employee(models.Model):
    
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=10)
    description = models.TextField()
    