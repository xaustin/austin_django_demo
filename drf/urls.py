# -*- coding: utf-8 -*-
__author__ = '许仕强'
# @Time    : 2018/8/3 14:08
# @Email   : austin@canway.net
from django.conf.urls import url
from django.views.static import serve
# from rest_framework.documentation import include_docs_urls
from .views import GoodsListView

urlpatterns = [
    url(r'^goods_list/', GoodsListView.as_view(), name="goods-list"),    # 登录页
]
