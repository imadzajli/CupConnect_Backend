from rest_framework import serializers
from .models import *

c = 00


class stadiumsseria(serializers.ModelSerializer):
    class Meta:
        model = stadiums
        fields = (
            "id",
            "name",
            "capacity",
            "city",
            "country",
            "desc",
            "cost",
            "picture",
        )


class userseria(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ("id", "username", "email", "password", "gender", "phone", "country")


class hotelseria(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "id",
            "name",
            "description",
            "min_price",
            "max_price",
            "stad"
        )

# lets creat a json to return data = ['name','capacity','city','country','desc','cost','picturesx7']
