#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 10:17
# @Author  : readExcel
# ##读取表格数据，返回的是一个列表，里面的数据以字典格式存放，通过索引得到字典然后取字典的值

#导入数据驱动模块xlsx
import xlrd
#创建类
class ExcelUtil(object):
    # 此参数为主程序传输过来
    def __init__(self, excelPath, sheetName="Sheet1"):
        # 打开excel文件
        self.data = xlrd.open_workbook(excelPath)
        # 获取excel文档中所有的sheet
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        #判断，如果第一个sheet行数小于1行，抛出异常，结束程序
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            #设置空list，用来存储文件中的数据
            r = []
            #设置起始值
            j = 1
            #因为第一行是标题所以总行数要-1
            for i in list(range(self.rowNum-1)):
                #创建空对象
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2

                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == "__main__":
    excelPath ='../data/textcase01.xlsx'
    sheetName = "Sheet1"
    data = ExcelUtil(excelPath, sheetName)
    for i in data.dict_data():
        print(i)
        print(type(i))


# class ExcelUtil():
#      def __init__(self, excelPath, sheetName="Sheet1"):
#          self.data = xlrd.open_workbook(excelPath)
#          self.table = self.data.sheet_by_name(sheetName)
#          # 获取第一行作为key值
#          # 获取总行数
#          self.rowNum = self.table.nrows
#          # 获取总列数
#          self.colNum = self.table.ncols
#      def dict_data(self):
#
#          if self.rowNum > 1:
#              #获取第一列的内容，列表格式
#              keys = self.table.row_values(0)
#              #print(keys)
#              listApiData = []
#              #获取每一行的内容，列表格式
#              for col in range(1,self.rowNum):
#                  values = keys.row_values(col)
#                  # keys，values这两个列表一一对应来组合转换为字典
#                  api_dict = dict(zip(keys, values))
#                  #print(api_dict)
#                  listApiData.append(api_dict)
#
#              return listApiData
#          else:
#              print("表格未填写数据")
#              return None
#
# if __name__ == "__main__":
#     excelPath = r"C:\Users\Administrator\PycharmProjects\untited4\Apitest\data\textcase01.xlsx"
#     sheetName = "Sheet1"
#     data = ExcelUtil(excelPath, sheetName)
#     for i in data.dict_data():
#         print(i)
#         print(type(i))


