from rest_framework import viewsets
from .models import Category, Movie
from .serializers import CategorySerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer
