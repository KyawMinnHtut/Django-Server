from rest_framework import viewsets
from .models import Live
from .serializers import LiveSerializer


# Create your views here.
class LiveViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Live.objects.all().order_by('-id')
    serializer_class = LiveSerializer
