from django.db import models
from django.contrib.auth.models import AbstractUser

class Reader(AbstractUsed):
    username = models.CharField(max_length = 100, blank =True, null = False)

    def __str__(self):
        return self.username
    

# Create your models here.
