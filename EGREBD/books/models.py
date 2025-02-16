from django.db import models

class Books(models.Model):
    Title = models.CharField(max_length=50 , null = False)
    AddDate = models.DateField( auto_now=False, auto_now_add=True)
    Author = models.CharField(max_length=30, null = True)

    def __str__(self):
        return self.Title
    
# Create your models here.
