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
    
class FileConvert(models.Model):
    fileName = models.CharField(max_length=100)
    fileType = models.CharField(max_length=100)
    file = models.FileField(upload_to= "./images/convert/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("fileMame: {0}, \n fileType: {1}, \n Uploaded At: {2} ".format(self.fileName, self.fileType, self.uploaded_at))
    
class Classify(models.Model):
    fileName = models.CharField(max_length=100)
    fileType = models.CharField(max_length=100)
    img = models.ImageField(upload_to="./images/classify/")

    def __str__(self):
        return self.fileName
    
class Segment(models.Model):
    fileName = models.CharField(max_length=100)
    fileType = models.CharField(max_length=100)
    img = models.ImageField(upload_to="./images/segment/")

    def __str__(self): 
        return self.fileName
    