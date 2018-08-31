# -*- coding: utf-8 -*-
__author__ = '许仕强'
# @Time    : 2018/8/3 17:55
# @Email   : austin@canway.net
import requests


def requests_post():
    post_url = 'http://127.0.0.1:9000/goods/add_post'
    params = {
        "name": "11111",
        "click_num": "222222",
        "add_time": "2018-08-03 15:03:55",
    }
    request = requests.post(post_url, params=params)
    # print request.content
    print request.status_code


if __name__ == '__main__':
    requests_post()