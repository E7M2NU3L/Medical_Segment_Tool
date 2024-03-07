from django.urls import path
from .views import home, classify,logout_user, Classified_output, segment, Segmented_output, login_user, project, register, convert
from .views import converted_image

urlpatterns = [
    path('', home, name="home"),
    path('classify', classify, name="classify"),
    path('classify/classified_output', Classified_output, name="classified_output"),
    path('segment', segment, name="segment"),
    path('segment/segmented_output', Segmented_output, name="segmented_output"),
    path('login', login_user, name="login"),
    path('project', project, name="project"),
    path('register', register, name="register"),
    path('logout', logout_user, name="logout"),
    path('convert', convert, name = "convert"),
    path('convert/output', converted_image, name="convert_download")
]