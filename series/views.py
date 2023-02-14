from rest_framework import viewsets
from .models import Series
from .serializers import SeriesSerializer


# Create your views here.
class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Series.objects.all().order_by('-id')
    serializer_class = SeriesSerializer