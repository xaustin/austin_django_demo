# -*- coding: utf-8 -*-
__author__ = '许仕强'
# @Time    : 2018/8/3 14:35
# @Email   : austin@canway.net
from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"
    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # add_time = serializers.DateTimeField()
    # print name
    #
    # def create(self, validated_data):
    #     return Goods.objects.create(**validated_data)
