from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]