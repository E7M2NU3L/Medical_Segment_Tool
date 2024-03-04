from django.db import models


# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length = 40)
    password = models.CharField(max_length = 40)

    def __str__(self) -> str:
        return self.email
    
class ImageToJpeg(models.Model):
    FileName = models.CharField(max_length = 30)
    img = models.ImageField(upload_to= "./images/img_to_jpeg/")

    def __str__(self) -> str:
        return self.FileName
    
class DicomClassify(models.Model):
    FileName = models.CharField(max_length = 30)
    img = models.ImageField(upload_to= "./images/dicom_classified/")

    def __str__(self) -> str:
        return self.FileName
    
class Segment(models.Model):
    FileName = models.CharField(max_length = 40)
    Nifti_file = models.ImageField(upload_to= "./nifti/segment_input/")

    def __str__(self) -> str:
        return self.FileName
