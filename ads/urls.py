from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'home', views.AdsViewSet)
router.register(r'image', views.ImageAdsViewSet)
router.register(r'text', views.TextAdsViewSet)

urlpatterns = [
    path('', include(router.urls))
]