from django.db import models

# Create your models 

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return (f'{self.email, self.first_name, self.last_name}')
    

class Segment(models.Model):
    FileName = models.CharField(max_length=100)
    File = models.ImageField(upload_to="./images/segment/")

    def __str__(self): 
        return self.fileName