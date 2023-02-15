from rest_framework import viewsets
from .models import Series, Category
from .serializers import SeriesSerializer, CategorySerializer


# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Series.objects.all().order_by('-id')
    serializer_class = SeriesSerializer
