# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
# @Software: PyCharm
from Interface.feng import reques
reques=reques()
class TestApi(object):
	def __init__(self,url,key,connent,fangshi):
		self.url=url
		self.key=key
		self.connent=connent
		self.fangshi=fangshi
	def testapi(self):
		if self.fangshi in ['POST', "GET"]:
			self.parem = {'key': self.key, 'info': self.connent}
			r=reques.post(self.url,self.parem)
		return r
	def getcode(self):
		return self.testapi()['code']
	def getJson(self):
		return self.testapi()