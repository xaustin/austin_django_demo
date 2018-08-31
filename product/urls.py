# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^count_book/$', views.count_book, name="count_book"),    # 登录页
]