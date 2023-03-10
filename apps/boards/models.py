from django.core.validators import MinValueValidator
from django.db import models

class Cartegory(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

class Board(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(validators=[MinValueValidator(0)], default=0)
