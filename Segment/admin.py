from django.contrib import admin

# Register your models here.
from .models import Users, Segment, DicomClassify, ImageToJpeg

admin.site.register(Users)
admin.site.register(Segment)
admin.site.register(DicomClassify)
admin.site.register(ImageToJpeg)

