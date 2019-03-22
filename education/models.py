from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Formation(models.Model):
    description = models.CharField(max_length=200, default='String')
    encadrant = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)



