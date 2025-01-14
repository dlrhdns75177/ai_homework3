from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    #nickname = models.CharField(max_length=50)
    #intro = models.TextField()
