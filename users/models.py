from django.db import models
from django.contrib.auth.hashers import make_password
class User(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('employee', 'Employee'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
