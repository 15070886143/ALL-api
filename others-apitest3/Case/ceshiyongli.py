# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @Site    : 
# @File    : ceshiyongli.py
# @Software: PyCharm
import unittest,os
from  Public import BSTestRunner
from  Interface.get_excel import datacel
from  Interface.testFengzhuang import TestApi
listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
class Testinface(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testinterface(self):
        list_pass = 0
        list_fail = 0
        list_json = []
        listrelust=[]
        listurls=[]
        listkeys=[]
        listids=[]
        listconeents=[]
        listfangshis=[]
        listqiwangs=[]
        listnames=[]
        for i in range(len(listurl)):
            api=TestApi(url=listurl[i],key=listkey[i],connent=listconeent[i],fangshi=listfangshi[i])
            apicode=api.getcode()
            apijson=api.getJson()
            if apicode==int(listqiwang[i]):
                listrelust.append('pass')
                list_pass += 1
            else:
                list_fail+=1
                listrelust.append('fail')
            list_json.append((apijson))
            listnames.append(listname[i])
            listqiwangs.append(listqiwang[i])
            listfangshis.append(listfangshi[i])
            listconeents.append(listconeent[i])
            listkeys.append(listkey[i])
            listurls.append(listurl[i])
            listids.append(listid[i])
        return  list_fail,list_pass,list_json,listurls,listkeys,listconeents,listfangshis,listqiwangs,listids,listrelust,listnames
