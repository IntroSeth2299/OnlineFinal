from django.db import models
from users.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hire_date = models.DateField(auto_now_add=True)
    expertise = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username
