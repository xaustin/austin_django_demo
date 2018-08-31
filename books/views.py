# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.forms.models import model_to_dict
from django.db.models import Q


def book_index(request):
    return render(request, 'books/book_index.html')


# 增加
@csrf_exempt
@permission_required(u'books.添加书籍')  # 查看是否有权限(添加权限的例子)
def add_auth(request):
    if request.method == 'POST':
        author = request.POST.get('author', '')
        phone_num = request.POST.get('phone_num', '')
        email = request.POST.get('email', '')
        try:
            auth = Author()
            auth.author = author
            auth.phone_num = phone_num
            auth.email = email
            auth.save()
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# 查询所有的作者
def search_author(request):
    if request.method == 'GET':
        auth_list = Author.objects.filter(Q(school__isnull=False))
        # NO.1
        auth_info = [i.to_dic() for i in auth_list]
        # return HttpResponse(json.dumps(auth_info), content_type="application/json")
        return JsonResponse(auth_info, safe=False)
        # NO.2
        # from django.core import serializers
        # json_data = serializers.serialize('json', auth_list)
        # json_data = json.loads(json_data)
        # # return HttpResponse(json.dumps(json_data), content_type="application/json")
        # return JsonResponse(json_data, safe=False)
        # NO.3
        # from django.forms.models import model_to_dict
        # auth_info = []
        # for i in auth_list:
        #     json_dict = model_to_dict(i)
        #     auth_info.append(json_dict)
        # # return HttpResponse(json.dumps(auth_info), content_type='application/json')
        # return JsonResponse(auth_info, safe=False)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# 修改
@csrf_exempt
def edi_auth(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        author = request.POST.get('author')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')
        try:
            auth = Author.objects.get(id=id)
            auth.author = author
            auth.phone_num = phone_num
            auth.email = email
            auth.save()
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# 删除
@csrf_exempt
def del_auth(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            Author.objects.get(id=id).delete()
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


"""
以下为一对一、一对多、多对多关系理解
首先解释下这些概念
一对一：子表从母表中选出一条数据一一对应，母表中选出来一条就少一条，子表不可以再选择母表中已被选择的那条数据

一对多：子表从母表中选出一条数据一一对应，但母表的这条数据还可以被其他子表数据选择

多对多总结：
　　比如有多个孩子，和多种颜色、
　　每个孩子可以喜欢多种颜色，一种颜色可以被多个孩子喜欢，对于双向均是可以有多个选择


应用场景
一对一：一般用于某张表的补充，比如用户基本信息是一张表，但并非每一个用户都需要有登录的权限，
        不需要记录用户名和密码，此时，合理的做法就是新建一张记录登录信息的表，与用户信息进行一对一的关联，
        可以方便的从子表查询母表信息或反向查询

外键：有很多的应用场景，比如每个员工归属于一个部门，那么就可以让员工表的部门字段与部门表进行一对多关联，
      可以查询到一个员工归属于哪个部门，也可反向查出某一部门有哪些员工

多对多：如很多公司，一台服务器可能会有多种用途，归属于多个产品线当中，那么服务器与产品线之间就可以做成对多对，
        多对多在A表添加manytomany字段或者从B表添加，效果一致
"""


# 增加Colors
@csrf_exempt
def add_color(request):
    if request.method == 'POST':
        colors = request.POST.get('colors', '')
        try:
            Colors.objects.create(colors=colors)
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# --------------------------------- 以下为一对一关系 ----------------------------------
# OneToOne  add （一对一 增加）
@csrf_exempt
def add_ball(request):
    if request.method == 'POST':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # 增添数据的三种写法：
            # 写法1：
            # Ball.objects.create(color=Colors.objects.get(id=int(color_id)), description=description)
            # 写法2：
            # color_obj = Colors.objects.create(colors="黑")
            # ball_obj = Ball(color=color_obj, description="黑球")
            # ball_obj.save()
            # 写法3(字典导入)：
            color_obj = Colors.objects.create(colors="黑")
            ball_dic = {'description': "黑球"}
            Ball.objects.create(color=color_obj, **ball_dic)
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# OneToOne  delete （一对一 删除）
@csrf_exempt
def del_ball(request):
    if request.method == 'POST':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # Ball.objects.get(description="描述一").delete()  # 对象和QuerySet都有delete()方法
            # Colors.objects.filter(colors="蓝色").delete()
            Colors.objects.all().delete()  # 清空一张表
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
    return JsonResponse(result)


# OneToOne  modify （一对一 修改）
@csrf_exempt
def modify_ball(request):
    if request.method == 'POST':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # 方法一
            # color_obj = Colors.objects.get(colors="黑")  # .get()等同于.filter().first()
            # color_obj.colors = "灰"
            # color_obj.save()
            # Ball.objects.filter(description="黑球").update(color=color_obj,
            #                                                description="灰球")  # update(),delete()是QuerySet的方法
            # 方法二
            # 更新多条数据，把满足条件的球的description都变为灰球
            # 写法1：
            # Ball.objects.filter(color__colors="红").update(description="灰球")
            # 写法2：
            up_dic = {"description": "灰球"}
            Ball.objects.filter(id__gt=0).update(**up_dic)
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
    return JsonResponse(result)


# OneToOne  search （一对一 查询）
@csrf_exempt
def search_ball(request):
    if request.method == 'GET':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # 子表查询母表,找到红球对应的颜色
            # 写法1：
            # print(Ball.objects.get(
            #     description="红球").color.colors)  # 返回红，通过子表查询母表，
            # 写法："子表对象.母表表名的小写.母表字段名" ；通过Ball表查到description为"红球"，查找到对应colors
            # 写法2，反向从母表入手：
            # print(Colors.objects.get(
            #     ball__description="红球").colors)  # 返回红，通过子表查询母表，但形式上是从母表对象自身直接获取字段，
            # 写法："母表.objects.get(子表名小写__子表字段="xxx").母表字段名" ；效果和上边完全一致，另一种形式

            # 母表查询子表，找到红色对应的球的名字
            # 写法1：
            # print(Colors.objects.get(
            #     colors="红").ball.description)  # 返回红球，通过母表查询子表，写法："母表对象.子表表名的小写.子表字段名"；找到颜色为红色的Ball的description
            # 写法2，反向从子表入手：
            print(Ball.objects.get(
                color__colors="蓝色").description)  # 返回红球，通过母表查询子表，但形式上是从子表对象自身直接获取字段，
            # 写法："子表.objects.get(一对一的子表字段__母表字段="xxx").子表字段"；效果和上边完全一致，另一种形式
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
    return JsonResponse(result)


# --------------------------------- 以下为一对多关系 ----------------------------------
# ForeignKey add (一对多 增加)
@csrf_exempt
def add_clothes(request):
    if request.method == 'POST':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # Clothes.objects.create(color=Colors.objects.get(id=int(color_id)), description=description)
            # 增添子表数据，形式与一对一一致
            # 添加颜色为绿的服装：小帅哥
            # 方法1：
            # Clothes.objects.create(color=Colors.objects.get(colors="红色"), description="这里是描述信息")
            # 方法1补充：
            # Clothes.objects.create(color_id=Colors.objects.get(colors="红色").id, description="这里是描述信息")
            # 方法2：
            c_obj = Clothes(color=Colors.objects.get(colors="红色"), description="这里是描述信息")
            c_obj.save()
            # 方法3：字典方式录入..参考一对一
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# ForeignKey delete (一对多 删除)
@csrf_exempt
def del_clothes(request):
    if request.method == 'GET':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # Clothes.objects.get(description="描述内容").delete()  # 对象和QuerySet都有方法delete()
            Colors.objects.filter(colors="蓝色").delete()
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
    return JsonResponse(result)


# ForeignKey modify (一对多 修改)
@csrf_exempt
def modify_clothes(request):
    if request.method == 'POST':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # 颜色为红，description 改为 这里是更新的信息
            # 写法1：
            # Clothes.objects.filter(color__colors="红").update(description="这里是更新的信息")
            # 写法2：
            # Clothes.objects.filter(color_id=Colors.objects.get(colors="红").id).update(description="这里是更新的信息")
            # 写法3：
            colors_obj = Colors.objects.get(colors="红")
            colors_obj.clothes_set.filter(id__gte=1).update(description="这里是更新的信息")
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# ForeignKey search (一对多 查询)
@csrf_exempt
def search_clothes(request):
    if request.method == 'POST':
        # color_id = request.POST.get('color_id', '')
        # description = request.POST.get('description', '')
        try:
            # 外键表联合查询：
            # 外键子表查询母表,与一对一子表查询母表形式一致
            # 找到对象所属的颜色表中的颜色--返回:红
            # 写法1：
            # print(Clothes.objects.get(
            #     description="描述内容").color.colors)  # 返回红，通过子表查询母表，
            # 写法："子表对象.母表表名的小写.母表字段名" ；通过Clothes表查到description为"描述内容"，查找到对应colors
            # 写法2，反向从母表入手：
            # print(Colors.objects.get(
            #     clothes__description="描述内容").colors)  # 返回红，通过子表查询母表，
            # 但形式上是从母表对象自身直接获取字段，写法："母表.objects.get(子表名小写__子表字段="xxx").母表字段名" ；
            # 效果和上边完全一致，另一种形式

            # 外键母表查询子表,与一对一形式不同，因为母表为"多"，
            # 不能像一对一一样通过.get().子表.子表字段的方式获取，但与多对多母表查询子表一致
            # 找到颜色为红的所有服装--返回:[<Clothes: 描述内容>，]
            # # 写法1：
            # color_obj = Colors.objects.get(colors="红色")
            # print(color_obj.clothes_set.all())  # 注意：子表小写_set的写法,它实际上是一个QuerySet,可以用update,delete,all,filter等方法
            # 写法2：
            # print(Clothes.objects.filter(color=Colors.objects.get(colors="红")))
            # 写法2简便写法（推荐）：
            # print(Clothes.objects.filter(color__colors="红色"))  # 写法：filter(子表外键字段__母表字段='过滤条件')
            # 写法3：
            color_id = Colors.objects.get(colors="红色").id  # 通过母表获取到颜色为红的id
            print(Clothes.objects.filter(color_id=color_id))  # filter得到QuerySet,写法：filter(子表外键字段_母表主键=母表主键对象)
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# --------------------------------- 以下为多对多关系 ----------------------------------
# ManyToMany add、modify (多对多 增加、修改)
@csrf_exempt
def add_child(request):
    if request.method == 'POST':
        try:
            # 写法一
            # child_obj = Child.objects.create(name="小虎")  # 如果是已有用户，使用.get()
            # colors_obj = Colors.objects.all()  # 创建颜色表的所有颜色QuerySet对象
            # child_obj.favor.add(*colors_obj)  # 添加对应关系,将小虎和所有颜色进行关联，
            # 写法：子表对象.子表多对多字段.add(*QuerySet对象)
            # 写法二
            # child_obj = Child.objects.get(name="小虎")
            # colors_obj = Colors.objects.all()
            # child_obj.favor = colors_obj
            # child_obj.save()
            # 写法三
            # 让小虎喜欢黄色和蓝色(2种写法和上边一致，只展示一种写法)
            # child_obj = Child.objects.get(name="小虎")
            # colors_obj = Colors.objects.filter(colors__in=["蓝色", "红色"])
            # child_obj.favor = colors_obj
            # child_obj.save()
            # 写法四
            # child_obj = Child.objects.get(name="小虎")
            # colors_obj = Colors.objects.filter(colors__in=["蓝色", "红色"])
            # child_obj.favor.clear()  # 清空小虎已经喜欢的颜色
            # child_obj.favor.add(*colors_obj)  # add是追加模式，如果当前小虎已经喜欢绿色，
            # 那么执行后，小虎会额外喜欢蓝，黄
            # 写法五
            # 让小虎只喜欢蓝色
            # child_obj = Child.objects.get(name="小虎")
            # colors_obj = Colors.objects.get(colors="蓝色")
            # child_obj.favor.clear()
            # child_obj.favor.add(colors_obj)  # 此处没有*     .add(),.remove(),.update(),.delete(),.clear()

            # 写法六
            # 让喜欢蓝色的人里添加小虎,可以用上边的方法，一个效果，让小虎喜欢蓝色，下边介绍反向插入(从母表入手)的写法
            # child_obj = Child.objects.get(name="小虎")
            # colors_obj = Colors.objects.get(colors="红色")
            # colors_obj.child_set.add(child_obj)  # 从colors表插入小虎，写法：母表对象.子表名小写_set.add(子表对象)。
            #  让喜欢蓝色的child_set集合添加name="小虎"
            # 写法七
            # 让所有人都喜欢蓝色
            children_obj = Child.objects.all()
            print Colors.objects.all()
            colors_obj = Colors.objects.get(colors="红色")
            colors_obj.child_set.add(*children_obj)
            # 关于_set写法，究竟什么时候使用_set,简单记忆，只有子表才有"子表名小写_set"的写法，得到的是一个QuerySet集合，后边可以接.add(),.remove(),.update(),.delete(),.clear()
            # 另外备注一下，colors_obj.child_set.clear()是让所有人喜欢的颜色里去掉蓝色，colors_obj.child_set.all().delete()是删除.child_set的所有人
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# ManyToMany delete (多对多 删除)
@csrf_exempt
def del_child(request):
    if request.method == 'POST':
        try:
            # 删除子表与母表关联关系
            # 让小虎不喜欢任何颜色
            # 写法1：
            # child_obj = Child.objects.get(name="小虎")
            # colors_obj = Colors.objects.all()
            # child_obj.favor.remove(*colors_obj)
            # # 写法2：
            # child_obj = Child.objects.get(name="小虎")
            # child_obj.favor.clear()
            #
            # # 删除母表与子表关联关系
            # # 让所有人不再喜欢蓝色
            # # 写法1：
            # children_obj = Child.objects.all()
            # colors_obj = Colors.objects.get(colors="蓝色")
            # colors_obj.child_set.remove(*children_obj)
            # # 写法2：
            # colors_obj = Colors.objects.get(colors="蓝色")
            # colors_obj.child_set.clear()

            # 删除子表数据
            # 喜欢蓝色的所有人都删掉
            # colors_obj = Colors.objects.get(colors="蓝")
            # colors_obj.child_set.all().delete()  # 注意有.all()
            # 删除所有child
            Child.objects.all().delete()
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


# ManyToMany search (多对多 查询)
@csrf_exempt
def search_child(request):
    if request.method == 'POST':
        try:
            # 多对多子表查询母表,查找小明喜欢哪些颜色--返回:[<Colors: 红>, <Colors: 黄>, <Colors: 蓝>]
            # 与一对多子表查询母表的形式不同，因为一对多，查询的是母表的“一”；多对多，查询的是母表的“多”
            # 写法1：
            # child_obj = Child.objects.get(name="小明")  # 写法：子表对象.子表多对多字段.过滤条件(all()/filter())
            # print(child_obj.favor.all())
            # 写法2，反向从母表入手：
            # print(Colors.objects.filter(child__name="小明"))  # 母表对象.filter(子表表名小写__子表字段名="过滤条件")

            # 多对多母表查询子表,查找有哪些人喜欢黄色--返回:[<Child: 小明>]
            # 与一对多母表查询子表的形式完全一致，因为查到的都是QuerySet，一对多和多对多，都是在查询子表的“多”
            # 写法1：
            # color_obj = Colors.objects.get(colors="黄")
            # print(color_obj.child_set.all())
            # 写法2：
            # print(Child.objects.filter(favor=Colors.objects.get(colors="黄")))
            # 写法2简便写法(推荐):
            # print(Child.objects.filter(favor__colors="黄"))  # 写法：filter(子表外键字段__母表字段='过滤条件')
            # 写法3：
            color_id = Colors.objects.get(colors="黄色").id  # 通过母表获取到颜色为红的id
            print(Child.objects.filter(
                favor=color_id))  # filter得到QuerySet,写法：filter(子表外键字段=母表主键对象),此处和一对多略有不同，是子表外键字段而不是外键字段_母表主键
            result = {'result': 'true'}
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)


from django.conf import settings
from django.core.cache import cache


# read cache user id
def read_from_cache(self, user_name):
    key = 'user_id_of_'+user_name
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data


# write cache user id
def write_to_cache(self, user_name):
    key = 'user_id_of_' + user_name
    cache.set(key, json.dumps(user_name), settings.NEVER_REDIS_TIMEOUT)
