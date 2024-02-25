from django.urls import path
from .views import *

urlpatterns=[
    path("",home),
    path("api/stadiums",stadiums_view.as_view()),
]
