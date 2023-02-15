from rest_framework import serializers
from .models import Series, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        exclude = ['id']
        depth = 2
    
