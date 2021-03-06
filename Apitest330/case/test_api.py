#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 16:54
# @Author  : case
import unittest
import ddt
import os
import requests
from Apitest330.common import base_api
from Apitest330.common import readExcel
from Apitest330.common import write


curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "demotext.xlsx")
# 复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xlsx")
testdata = readExcel.ExcelUtil(testxlsx).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了
        write.copy_excel(testxlsx, reportxlsx) # 复制xlsx
    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = base_api.send_requests(self.s, data)
        base_api.wirte_result(res, filename=reportxlsx)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s"%check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s"%res_text)
        # 断言
        self.assertIsNotNone(check , res_text)
        # if check in res_text:
        #     res["result"] = 'fali'
        # else:
        #     print("实际结果与期望结果不一致，请提bug！！")
if __name__ == "__main__":
    unittest.main()


