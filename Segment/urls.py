from django.urls import path
from .views import home, logout_user, segment, Segmented_output, login_user, project, register


urlpatterns = [
    path('', home, name="home"),
    path('segment', segment, name="segment"),
    path('segment/segmented_output', Segmented_output, name="segmented_output"),
    path('login', login_user, name="login"),
    path('project', project, name="project"),
    path('register', register, name="register"),
    path('logout', logout_user, name="logout"),
]