from rest_framework import serializers
from .models import Ads, ImageAds, TextAds

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        exclude = ['id']

class ImageAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAds
        exclude = ['id']

class TextAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAds
        exclude = ['id']