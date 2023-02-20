from django.urls import path
#from rest_framework import routers
from . import views
#from django.conf.urls import url

#router = routers.DefaultRouter()
#router.register(r'', views.CustomUserViewSet)

urlpatterns = [
#    path(r'^authenticate/', CustomObtainAuthToken.as_view()),
    path('', views.CreateUser.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]
