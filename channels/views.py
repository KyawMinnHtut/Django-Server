from rest_framework import viewsets
from .models import Channels, Category
from .serializers import ChannelSerializer, CategorySerializer


# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Channels.objects.all().order_by('title')
    serializer_class = ChannelSerializer
