from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='instructor_profiles/')

    def __str__(self):
        return self.user.username
