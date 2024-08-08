from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="shopping_list"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    