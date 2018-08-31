# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book_index/$', views.book_index, name="book_index"),    # 登录页
    url(r'^add_auth/$', views.add_auth, name="add_auth"),    # 添加作者
    url(r'^search_author/$', views.search_author, name="search_author"),    # 查询作者
    url(r'^edi_auth/$', views.edi_auth, name="edi_auth"),    # 修改作者
    url(r'^del_auth/$', views.del_auth, name="del_auth"),    # 删除作者
    url(r'^add_color/$', views.add_color, name="add_color"),    # add_color
    # 一对一
    url(r'^add_ball/$', views.add_ball, name="add_ball"),    # add_ball
    url(r'^del_ball/$', views.del_ball, name="del_ball"),    # del_ball
    url(r'^modify_ball/$', views.modify_ball, name="modify_ball"),    # del_ball
    url(r'^search_ball/$', views.search_ball, name="search_ball"),    # search_ball
    # 一对多
    url(r'^add_clothes/$', views.add_clothes, name="add_clothes"),    # add_clothes
    url(r'^del_clothes/$', views.del_clothes, name="del_clothes"),    # del_clothes
    url(r'^modify_clothes/$', views.modify_clothes, name="modify_clothes"),    # modify_clothes
    url(r'^search_clothes/$', views.search_clothes, name="search_clothes"),    # search_clothes
    # 多对多
    url(r'^add_child/$', views.add_child, name="add_child"),  # add_clothes
    url(r'^del_child/$', views.del_child, name="del_child"),  # del_child
    url(r'^search_child/$', views.search_child, name="search_child"),  # search_child
]
