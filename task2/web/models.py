from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    topic = models.CharField(max_length=200)
    text = models.TextField()