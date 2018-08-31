# -*- coding: utf-8 -*-
from django.http import JsonResponse
from models import *
from django.views.decorators.csrf import csrf_exempt


# 利用自己写的Manager方法,
@csrf_exempt
def count_book(request):
    result = {}
    if request.method == 'GET':
        key_word = request.POST.get('key_word', '')
        try:
            book_count = Book.objects.title_count(key_word)
            result["result"] = True
            result["count"] = book_count
            return JsonResponse(result)
        except Exception, e:
            print Exception, ":", e
            result = {'result': 'false'}
            return JsonResponse(result)
    else:
        result = {'result': '请求错误'}
        return JsonResponse(result)
