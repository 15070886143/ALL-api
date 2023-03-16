#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 16:20
# @Author  : base_api
import json
import requests
from Apitest330.common.readExcel import ExcelUtil
from Apitest330.common.write import copy_excel, Write_excel

def send_requests(s,testdata):
    method = testdata["method"]
    url = testdata["url"]
    priority = testdata["priority"]
    print(priority)
    test_nub = testdata["id"]
    try:
        params = eval(testdata["params"])
    except:
        params = None
    try:
        headers = eval(testdata["headers"])
        print(f"请求头部{headers}")
    except:
        headers = None
    type = testdata["type"]
    print(f"*********正在执行用例*********{test_nub}*******************")
    print(f"请求方式：{method},请求url：{url}")
    print(f"get请求参数：{params}")
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    body = json.dumps(bodydata) if type == "json" else bodydata
    if method == "post":
        print(f"post请求body类型为：{type}，body内容为：{body}")
    verify = False
    res ={}
    try:
        r= s.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            data=body,
            verify=verify
        )
        print(f'页面返回信息：{r.content.decode("utf-8")}')
        print(f"excel文件返回信息：{testdata['checkpoint']}")
        res["id"] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res['statuscode'] = str(r.status_code)
        res['text'] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())
        res["error"] = res['text'] if res['statuscode']!= "200" else ""
        res["msg"] = ""
        res["result"] = "pass" if testdata["checkpoint"] in res["text"] else "fail"
        print(f'测试结果为：{test_nub}---->{res["result"]}')
        return res
    except  Exception as msg:
        res["msg"] = str(msg)
        return res
def wirte_result(result,filename = r'../data/textcase02.xlsx'):
    row_nub = result['rowNum']
    wt = Write_excel(filename)
    wt.write(row_nub,8,result['statuscode'])
    wt.write(row_nub,12,result['times'])
    wt.write(row_nub,9,result['error'])
    wt.write(row_nub,10,result['result'])
    wt.write(row_nub,12,result['msg'])


if __name__=='__main__':
    data = ExcelUtil('../data/textcase01.xlsx').dict_data()
    for i in data:
        s = requests.session()
        res = send_requests(s,i)
        copy_excel('../data/textcase01.xlsx', '../data/textcase02.xlsx')
        wirte_result(res, filename='../data/textcase02.xlsx')







