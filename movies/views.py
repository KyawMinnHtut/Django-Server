from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Movie
from .serializers import CategorySerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = Category.objects.all().order_by('-id')[:50]
    serializer_class = CategorySerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer

class FilteredMovieView(APIView):
    permission_classes = (IsAuthenticated,)
    @staticmethod
    def get(request, category_id):
        items = Movie.objects.filter(category_id=category_id).order_by('-id')
        serializer_class = MovieSerializer(items, many=True)
        return Response(serializer_class.data)
