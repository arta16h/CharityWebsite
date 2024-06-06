from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model) :
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    keywords = models.TextField(null=True, blank=True)
    imageUrl = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.title}"