from rest_framework import serializers
from .models import Live

# class LiveLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LiveLinks
#         fields = "__all__"

class LiveSerializer(serializers.ModelSerializer):
    # links = serializers.PrimaryKeyRelatedField(many= True, read_only=True)
    # links = LiveLinkSerializer(many=True, read_only=True)
    class Meta:
        model = Live
        # fields = "__all__"
        exclude = ['id']
        depth = 1
        # fields = ('league', 'date', 'time', 'himg', 'aimg', 'teams', 'hteam', 'ateam', 'hotmat', 'links')