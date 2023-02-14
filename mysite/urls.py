"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

from django.contrib import admin
from django.urls import path, include
from myapp import urls as myapp_urls
from highlights import urls as highlight_urls
from channels import urls as channel_urls
from news import urls as news_urls
from movies import urls as movie_urls
from series import urls as seires_urls
from ads import urls as ads_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/live/', include(myapp_urls)),
    path('api/highlight/', include(highlight_urls)),
    path('api/channel/', include(channel_urls)),
    path('api/news/', include(news_urls)),
    path('api/movies/', include(movie_urls)),
    path('api/series/', include(seires_urls)),
    path('api/ads/', include(ads_urls)),
]
