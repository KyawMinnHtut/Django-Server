from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows users to be viewed.'''
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer
