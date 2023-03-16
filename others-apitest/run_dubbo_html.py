# -*- coding: utf-8 -*-
# @Author  : leizi
import os,datetime,time
from testCase.dubbocase import testdubbointerface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from Public.Dingtalk import send_ding
def start_dubbo_case():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\test_case_data\\dubbocase.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testdubbointerface()
    filepath =os.path.join(basdir+'\\test_Report\\%s-result.html'%day)
    if os.path.exists(filepath) is False:
        os.system(f'touch {filepath}')
    endtime=datetime.datetime.now()
    createHtml(titles='dubbo接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)
    contec = f'dubbo接口自动化测试完成，测试通过:{list_pass},测试失败：{list_fail}，异常:{list_exption},未知错误：{list_weizhi},详情见：{filepath}'
    send_ding(content=contec)
if __name__ == '__main__':
    start_dubbo_case()