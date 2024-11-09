from django.db import models
from django.utils import timezone
# Create your models here.
class Entry(models.Model):
  header = models.CharField(max_length=100)
  entry = models.TextField()
  timestamp = models.DateTimeField(default=timezone.now)