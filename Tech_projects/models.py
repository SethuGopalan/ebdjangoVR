from django.db import models

class Tech_project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image= models.FilePathField(path="/img")
