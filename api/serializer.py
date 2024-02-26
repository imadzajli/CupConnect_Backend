from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

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
            "latitude",
            "longitude",
        )


class userseria(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "gender",
            "phone",
            "country",
        )

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        # Adding the below line made it work for me.
        instance.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password
            instance.set_password(password)
        instance.save()
        return instance


class hotelseria(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "id",
            "name",
            "properties",
            "min_price",
            "max_price",
            "latitude",
            "longitude",
            "image",
            "map",
            "review",
            "address",
            "hotel_id",
            "stad",
        )


class cityseria(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = (
            "id",
            "name",
            "stad_id",
            "desc",
            "population",
            "creation_date",
            "transport",
        )


class placeseria(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = (
            "id",
            "name",
            "city_id",
            "desc",
            "location",
            "distance_from_stadium",
            "image",
        )


class disheseria(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = ("id", "name", "city_id", "desc", "image")
