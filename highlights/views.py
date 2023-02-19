from rest_framework import viewsets
from .models import HighLight
from .serializers import LiveSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HighLightViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = HighLight.objects.all().order_by('-id')
    serializer_class = LiveSerializer
