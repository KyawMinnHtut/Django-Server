from rest_framework import viewsets
from .models import Live
from .serializers import LiveSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LiveViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = Live.objects.all().order_by('-id')
    serializer_class = LiveSerializer
