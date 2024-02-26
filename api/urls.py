from django.urls import path
from .views import *

urlpatterns = [
    path("migrate", home),
    path("api/hotel/<int:stad_id>", hotel_view.as_view()),
    path("api/stadium/", stadiums_view.as_view()),
    path("api/user/", user_view.as_view()),
    path("api/user/create/", create_user),
    path("api/user/getuser/<str:email>", get_user),
    path("api/user/update/<str:attribute>/<int:id>/<str:new_value>", update_user),
    path("api/city/", city_view.as_view()),
    path("api/city/<int:id>", get_city_by_stad),
    path("api/place/", place_view.as_view()),
    path("api/place/<str:city>", get_places_by_city),
    path("api/dishes/", dishe_view.as_view()),
    path("api/dishes/<str:cname>", get_dishe_by_city),
]
