from rest_framework import viewsets
from .models import Channels
from .serializers import ChannelSerializer


# Create your views here.
class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Channels.objects.all().order_by('title')
    serializer_class = ChannelSerializer
