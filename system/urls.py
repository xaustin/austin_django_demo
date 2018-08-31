# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.system_login, name="system_login"),    # 登录页
    url(r'^declare_index/$', views.declare_index, name="declare_index"),  # 系统首页
    url(r'^index/$', views.index, name="index"),
    url(r'^system_logout/$', views.system_logout, name="system_logout"),  # 退出系统
    url(r'^register/$', views.register, name="register"),  # 用户注册
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.active_user, name='active_user'),   # 注册验证
    url(r'^send_email/$', views.send_email, name="send_email"),  # 忘记密码
    url(r'^add_user/$', views.add_user, name="add_user"),  # 添加用户
    url(r'^add_group/$', views.add_group, name="add_group"),  # 添加组
    url(r'^add_user_group_rel/$', views.add_user_group_rel, name="add_user_group_rel"),  # 添加用户与组的关系
    url(r'^del_user_group_rel/$', views.del_user_group_rel, name="del_user_group_rel"),  # 删除用户与组的关系
    url(r'^group_user_info/$', views.group_user_info, name="group_user_info"),  # 获取组里有哪些用户
    url(r'^get_user_group/$', views.get_user_group, name="get_user_group"),  # 获取用户有哪些组
    url(r'^list_perm/$', views.list_perm, name="list_perm"),  # 获取权限列表
    url(r'^get_user_permission/$', views.get_user_permission, name="get_user_permission"),  # 获取用户有哪些权限
    url(r'^add_group_permission/$', views.add_group_permission, name="add_group_permission"),  # 添加组权限
    url(r'^user_add_permission/$', views.user_add_permission, name="user_add_permission"),  # 添加用户权限

]
