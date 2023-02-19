from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    '''API endpoint that allows users to be viewed.'''
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer
