from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'', views.CustomUserViewSet)

urlpatterns = [
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
    path('', include(router.urls))
]
