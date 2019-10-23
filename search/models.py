from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=40, primary_key=True)
    freq = models.IntegerField()