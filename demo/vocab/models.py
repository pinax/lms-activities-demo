from django.db import models


class Vocabulary(models.Model):
    word = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
