from django.db import models

class Demo(models.Model):
    field = models.CharField(max_length=100)
