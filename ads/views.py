from rest_framework import viewsets
from .models import Ads, ImageAds, TextAds
from .serializers import AdsSerializer, ImageAdsSerializer, TextAdsSerializer


# Create your views here.
class AdsViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = Ads.objects.all().order_by('-id')
    serializer_class = AdsSerializer

# Create your views here.
class ImageAdsViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = ImageAds.objects.all().order_by('-id')
    serializer_class = ImageAdsSerializer

class TextAdsViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = TextAds.objects.all().order_by('-id')
    serializer_class = TextAdsSerializer