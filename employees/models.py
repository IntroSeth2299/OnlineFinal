from django.db import models
from users.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
