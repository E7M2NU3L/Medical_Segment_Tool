from django.contrib import admin
from .models import Classify, Segment, FileConvert

# Register your models here
admin.site.register(Classify)
admin.site.register(FileConvert)
admin.site.register(Segment)
