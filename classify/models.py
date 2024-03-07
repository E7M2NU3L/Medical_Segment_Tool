from django.db import models

# Create your models here.

class Classify(models.Model):
    fileName = models.CharField(max_length=100)
    img = models.ImageField(upload_to="./images/classify/")

    def __str__(self):
        return self.fileName
    