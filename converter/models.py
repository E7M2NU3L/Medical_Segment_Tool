from django.db import models

class FileConvert(models.Model):
    fileName = models.CharField(max_length=100)
    fileType = models.CharField(max_length=100)
    file = models.FileField(upload_to= "./images/convert/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("fileMame: {0}, \n fileType: {1}, \n Uploaded At: {2} ".format(self.fileName, self.fileType, self.uploaded_at))
