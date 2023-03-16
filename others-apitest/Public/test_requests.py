# -*- coding: utf-8 -*-
# @Author  : leizi
import requests,json
from Public.log import LOG,logger
@logger('requests封装')
class requ():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
    def get(self, url,params):#get消息
        try:
            r = requests.get(url, params=params,headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info(f'get请求出错，出错原因:{e}')
            return {'code': 1, 'result': f'get请求出错，出错原因:{e}'}
    def post(self, url, params):#post消息
        data = json.dumps(params)
        try:
            r =requests.post(url,params=data,headers=self.headers)
            json_response = json.loads(r.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info(f'post请求出错，出错原因:{e}')
            return {'code': 1, 'result': f'post请求出错，出错原因:{e}'}
    def delfile(self,url,params):#删除的请求
        try:
            del_word=requests.delete(url,params=params,headers=self.headers)
            json_response=json.loads(del_word.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info(f'del请求出错，出错原因:{e}')
            return {'code': 1, 'result': f'del请求出错，出错原因:{e}'}
    def putfile(self,url,params):#put请求
        try:
            data=json.dumps(params)
            me=requests.put(url,data)
            json_response=json.loads(me.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info(f'put请求出错，出错原因:{e}')
            return {'code': 1, 'result': f'put请求出错，出错原因:{e}'}