from rest_framework import serializers
from .models import Channels

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        exclude = ['id']