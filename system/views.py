# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import Permission
from forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from tokenvalidate import *
from random import choice
import string
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.backends import ModelBackend
from system.models import User
from django.contrib.auth.models import Group
import simplejson
from datetime import date, datetime


# 重写登录验证方法，支持账户名和邮箱登陆，可扩展其他登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 设置登录页
@csrf_exempt
def main_page(request):
    return render(request, "system/declare_login.html", locals())


# 登录
@csrf_exempt
def system_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            authentication = CustomBackend()
            user = authentication.authenticate(request, username=username, password=password)  # 验证user
            if user is not None:
                if user.is_active:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'  # 给user手动添加backend
                    auth.login(request, user)  # 登录
                    next_url = reverse('index')
                    return HttpResponseRedirect(next_url)
                else:
                    errmsg = "用户未激活，请激活后重新登录。"
                    return render(request, "system/declare_login.html", locals())
            else:
                errmsg = "账号密码信息有误，请重新输入。"
                return render(request, "system/declare_login.html", locals())
        else:
            return render(request, "system/declare_login.html")
    else:
        return render(request, "system/declare_login.html")


# 注销
@login_required
@csrf_exempt
def system_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/auth/login')


# 登录进的首页面
@csrf_exempt
def declare_index(request):
    return render(request, "system/declare_index.html", locals())


def index(request):
    request.session.set_expiry(0)  # 当浏览器关闭时，session失效
    url = reverse('declare_index')
    return redirect(url)


# 用户注册
@csrf_exempt
def register(request):
    result = {'result': ''}
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        qq_number = request.POST.get('qq_number')
        user = User.objects.filter(username=username)
        if user:
            err_msg = "同名用户已存在，请重新注册！"
            result["result"] = err_msg
        user_email = User.objects.filter(email=email)
        if user_email:
            err_msg = "该邮箱已存在，请重新注册！"
            result["result"] = err_msg
        else:
            user = User()
            user.set_password(password)
            user.email = email
            user.username = username
            user.phone_number = phone_number
            user.qq_number = qq_number
            user.is_active = False

            try:
                global token_confirm
                token = token_confirm.generate_validate_token(username)
                message = "\n".join([u'{0},恭喜您注册成功！有效期为1个小时，'.format(username), u'请访问该链接，完成用户验证:',
                                     '/'.join(['http://', django_settings.DOMAIN, 'auth/activate', token]),
                                     u'', u'', u'', u'该邮件为系统自动发出，请勿直接回复。'])
                send_mail(u'注册用户验证信息', message, 'xsq0109@sohu.com', [email, ], fail_silently=False)
            except Exception, e:
                print Exception, ":", e
            ture_msg = "提交成功，请到邮箱进行激活"
            user.save()
            result["result"] = ture_msg
    return JsonResponse(result)


# 注册邮箱验证函数
@csrf_exempt
def active_user(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except Exception, e:
        username = token_confirm.remove_validate_token(token)
        users = User.objects.filter(username=username)
        for user in users:
            user.delete()
        message = 1
        return render(request, 'system/message.html', locals())
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        message = 2
        return render(request, 'system/message.html', locals())
    user.is_active = True
    user.save()
    message = 3
    return render(request, 'system/message.html', locals())


# 邮箱找回密码
@csrf_exempt
def send_email(request):
    result = {'result': ''}
    if request.method == "POST":
        emailaddress = request.POST.get('emailaddress')
        if User.objects.filter(email=emailaddress):
            for i in User.objects.filter(email=emailaddress):
                # 生成随机密码
                def GenPassword(length=8, chars=string.ascii_letters + string.digits):
                    return ''.join([choice(chars) for i in range(length)])
                pawdtemp = GenPassword(8)
                i.set_password(pawdtemp)
                i.save()
                username = i.username
                message = "\n".join([u'{0},恭喜您，修改密码成功,新密码为'.format(username) + pawdtemp + u'，请牢记', ])
                send_mail(u'用户找回密码通知', message, 'xsq0109@sohu.com', [emailaddress, ], fail_silently=False)
                ture_msg = "修改成功,请去邮箱查收并使用新的密码登录"
                result["result"] = ture_msg

        else:
            ture_msg = "您的邮箱的账户注册信息没有找到"
            result["result"] = ture_msg
            return HttpResponse("您的邮箱的账户注册信息没有找到")
    else:
        ture_msg = "状态错误！"
        result["result"] = ture_msg
    return JsonResponse(result)


# TODO
# 添加人员（测试用）
@csrf_exempt
def add_user(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            user = User()
            user.set_password(password)
            user.username = user_name
            user.is_active = True
            user.save()
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': 'true'}
        return JsonResponse(result)


# TODO
# 组关系
# 添加组
@csrf_exempt
def add_group(request):
    result = {}
    if request.method == "POST":
        role_name = request.POST.get('name')
        try:
            if role_name:
                roles = Group.objects.filter(name=role_name).all()
                if len(roles) > 0:
                    result['error'] = '同名的角色项已存在，请修改角色名称。'
                else:
                    group = Group()
                    group.name = role_name
                    group.is_enable = True   # 该字段为因业务需要自添加的字段
                    group.save()
                    result = {'result': 'true'}
                return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': 'false'}
        return JsonResponse(result)


# TODO
# 添加人员与小组的关系
@csrf_exempt
def add_user_group_rel(request):
    if request.method == 'POST':
        try:
            group_id = request.POST.get('group_id')
            user_id = request.POST.get('user_id')
            group_info = Group.objects.get(id=group_id)
            User.objects.get(id=user_id).groups.add(group_info)
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误！'}
        return JsonResponse(result)


# TODO
# 删除人员与小组的关系
@csrf_exempt
def del_user_group_rel(request):
    if request.method == 'POST':
        try:
            group_id = request.POST.get('group_id')
            user_id = request.POST.get('user_id')
            group_info = Group.objects.get(id=group_id)
            User.objects.get(id=user_id).groups.remove(group_info)
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误！'}
        return JsonResponse(result)


# 时间格式进行转换
def __default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


# TODO
# 获得组里有哪些成员
@csrf_exempt
def group_user_info(request):
    if request.method == 'GET':
        try:
            group_id = request.GET.get('group_id')
            group_info = Group.objects.get(id=group_id)
            group_detail = []
            for row in group_info.user_set.all():
                group_detail.append({'username': row.username, 'id': row.id, 'date_joined': row.date_joined})
            json_data = simplejson.dumps(group_detail, default=__default)  # 转成json格式
            return HttpResponse(json_data, content_type="application/json")
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误！'}
        return JsonResponse(result)


# TODO
# 获得一个成员有哪些小组
@csrf_exempt
def get_user_group(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            current_user_set = User.objects.filter(id=user_id)
            current_group_set = Group.objects.filter(user=current_user_set)
            group_detail = []
            for row in current_group_set:
                group_detail.append({'name': row.name})
            json_data = simplejson.dumps(group_detail, default=__default)  # 转成json 格式的
            return HttpResponse(json_data, content_type="application/json")
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误！'}
        return JsonResponse(result)


# TODO
# 获取权限列表,用于将权限名称全部展示到页面上
def list_perm(request):
    perms = Permission.objects.filter(per_name__iregex=u'[\u4e00-\u9fa5]').order_by('cate', 'id').all()
    group_detail = []
    for row in perms:
        group_detail.append({'id': row.id, 'cate': row.cate, 'per_name': row.per_name, 'order': row.order})
    json_data = simplejson.dumps(group_detail, default=__default)  # 转成json格式
    return HttpResponse(json_data, content_type="application/json")


# TODO
# 获取当前用户的所有权限
def get_user_permission(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            user = User.objects.get(id=user_id)
            print user.get_all_permissions()  # 获得用户的全部权限
            if user.has_perm(u'books.添加书籍'):   # 验证是否有权限
                print "This user has the right to add books"
            if user.has_perm(u'books.删除书籍'):
                print "This user has the right to del books"
            if user.has_perm(u'books.添加出版社'):
                print "This user has the right to add press"
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误！'}
        return JsonResponse(result)


# TODO
# 添加组权限
@csrf_exempt
def add_group_permission(request):
    result = {}
    if request.method == 'GET':
        role = Group.objects.get(pk=1)
        pids = ['31']   # 这里是权限id 的列表 需要将权限的id传过来
        ps = Permission.objects.filter(per_name__iregex=u'[\u4e00-\u9fa5]').all()  # 匹配汉字
        for p in ps:
            if str(p.id) in pids:
                role.permissions.add(p)
            else:
                role.permissions.remove(p)
        result["result"] = True
        return JsonResponse(result)


# TODO
# 添加个人的单独的权限
@csrf_exempt
def user_add_permission(request):
    result = {}
    try:
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            user = User.objects.get(pk=user_id)
            pids = ['32']  # 这里是权限id 的列表 需要将权限的id传过来
            ps = Permission.objects.filter(per_name__iregex=u'[\u4e00-\u9fa5]').all()  # 匹配汉字
            for p in ps:
                if str(p.id) in pids:
                    user.user_permissions.add(p)
                else:
                    user.user_permissions.remove(p)
            result["result"] = True
            return JsonResponse(result)
        else:
            result["result"] = False
            return JsonResponse(result)
    except Exception, e:
        print Exception, ":", e
        result["result"] = False
        return JsonResponse(result)
