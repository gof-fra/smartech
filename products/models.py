from django.db import models


class Products(models.Model):
    code = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    active = models.CharField(max_length=100)


