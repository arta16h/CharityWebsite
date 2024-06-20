from django.db import models
from django.urls import reverse
from users.models import User
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
User = settings.AUTH_USER_MODEL    
class Blog(models.Model) :
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    keywords = models.TextField(null=True, blank=True)
    imageUrl = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.title}"
    
    def get_absolute_url(self) :
        return reverse('blog-detail', kwargs={'pk':self.pk})