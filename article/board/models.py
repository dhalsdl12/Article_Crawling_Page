from django.db import models

# Create your models here.
class SearchTerm(models.Model):
    term = models.CharField(max_length=255)
    