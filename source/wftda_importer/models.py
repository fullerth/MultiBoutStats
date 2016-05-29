from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50, null=True)
