"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField(blank=True, null=True)
    