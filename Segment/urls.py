from django.urls import path
from .views import home, classify, Classified_output, segment, Segmented_output, login, project, register
from django.http import HttpResponse

'''
url_patterns = [
    path('', home),
    path('classify', classify),
    path('classify/classified_output', Classified_output),
    path('segment', segment),
    path('segment/segmented_output', Segmented_output),
    path('login', login),
    path('project', project),
    path('register', register),
]

'''

url_patterns = [
    path('', HttpResponse("Hello Guys"))
]
