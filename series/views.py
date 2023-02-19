from rest_framework import viewsets
from .models import Series, Category
from .serializers import SeriesSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = Series.objects.all().order_by('-id')
    serializer_class = SeriesSerializer
