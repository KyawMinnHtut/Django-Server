from rest_framework import serializers
from .models import Channels, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        exclude = ['id']
