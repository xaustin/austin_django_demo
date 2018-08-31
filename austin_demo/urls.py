"""austin_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from system import views as sysviews
from drf.views import GoodsListView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', sysviews.main_page),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('system.urls')),
    url(r'^api/', include('books.urls')),
    url(r'^goods/', include('drf.urls')),
    url(r'^pro-api/', include('product.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^goods/', GoodsListView.as_view(), name="goods-list"),
]
