from rest_framework import viewsets
from .models import HighLight
from .serializers import LiveSerializer


# Create your views here.
class HighLightViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = HighLight.objects.all().order_by('-id')
    serializer_class = LiveSerializer
