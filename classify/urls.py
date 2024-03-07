from django.urls import path
from .views import classify, Classified_output

urlpatterns = [
    path('classify', classify, name="classify"),
    path('classify/classified_output', Classified_output, name="classified_output"),
]