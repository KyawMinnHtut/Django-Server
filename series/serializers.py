from rest_framework import serializers
from .models import Series

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        exclude = ['id']
        depth = 1
    