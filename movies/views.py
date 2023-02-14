from rest_framework import viewsets
from .models import Category, Movie
from .serializers import CategorySerializer, MovieSerializer


# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer