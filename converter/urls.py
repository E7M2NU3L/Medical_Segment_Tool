from django.urls import path
from .views import convert, converted_image

urlpatterns = [
    path('convert', convert, name='convert'),
    path('convert/output', converted_image, name= "output_conv"),
]