from .models import CustomUser
from rest_framework import serializers

#class CustomUserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = CustomUser
#        fields = ("id", "username", "password", "premium_date")

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", 'password')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "premium_date")
