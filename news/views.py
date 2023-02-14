from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer


# Create your views here.
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer
