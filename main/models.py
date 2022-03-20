from django.db import models

# Create your models here.
class contact_DB(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=10)
    message = models.TextField()