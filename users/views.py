from django.http import Http404
from .models import CustomUser
#from .serializers import CustomUserSerializer, CreateUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

# Create your views here.
#class CustomUserViewSet(viewsets.ModelViewSet):
#    '''API endpoint that allows users to be viewed.'''
#    queryset = CustomUser.objects.all().order_by('-id')
#    serializer_class = CustomUserSerializer

class CreateUser(APIView):
    #permission_classes = [AllowAny]

    def post(self, request, format='json'):
        print(request.data)
        data = request.data
        reg_serializer = CreateUserSerializer(data=data)
        if reg_serializer.is_valid():
            password = reg_serializer.validated_data.get('password')
            reg_serializer.validated_data['password']=make_password(password)
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404


    def get(self, request, pk, format='json'):
        user = self.get_object(pk)
        serializer = CustomUserDetailsSerializer(user)
        return Response(serializer.data)
