from django.urls import path
from .views import *

urlpatterns = [
    path("api/stadium/", stadiums_view.as_view()),
    path("api/user/", user_view.as_view()),
    path("api/user/create/", create_user),
    path("api/user/getuser/<str:email>", get_user),
]
