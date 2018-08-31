# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Row1(MiddlewareMixin):
    def process_request(self, request):
        print("中间件1请求")

    def process_response(self, request, response):
        print("中间件1返回")
        return response


class Row2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件2请求")
        # return HttpResponse("走")

    def process_response(self, request, response):
        print("中间件2返回")
        return response


class Row3(MiddlewareMixin):
    def process_request(self, request):
        print("中间件3请求")

    def process_response(self, request, response):
        print("中间件3返回")
        return response
