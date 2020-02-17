import json

import requests


class BasePage(object):
    def __init__(self):
        self.res = requests

    def send_requests(self, url, request_method, headers=None, boby=None, **kwargs):
        if request_method == 'get':
            r = self.res.get(url, headers=headers, params=boby, **kwargs)
            return r
        elif request_method == 'post':
            r = self.res.post(url, headers=headers, json=boby, **kwargs)  # 发送请求
            return r
        else:
            raise TypeError('不支持%s类型请求，请尝试post或者get方式' % request_method)




if __name__ == '__main__':
    bp = BasePage()
    url = 'http://127.0.0.1:5000/'
    request_method = 'get'
    r = bp.send_requests(url,request_method)
    r.raw
    print(r.raw)
