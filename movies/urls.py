from django.urls import path, include
from rest_framework import routers
from . import views
from .views import FilteredMovieView

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:category_id>/', FilteredMovieView.as_view())
]
