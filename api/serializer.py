from rest_framework import serializers
from .models import *

c=00

class stadiumsseria(serializers.ModelSerializer):
    class Meta:
        model = stadiums
        fields = ('id','name','capacity','city','country','desc','cost','picture')























# lets creat a json to return data = ['name','capacity','city','country','desc','cost','picturesx7']