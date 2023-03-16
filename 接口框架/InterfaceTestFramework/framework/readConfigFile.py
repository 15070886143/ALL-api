# coding=utf-8
import os
import codecs
import configparser

configPath = f'{os.path.abspath(os.curdir)}/testConfig/config.ini'


class ReadConfig:

    # 构造函数，读取配置文件
    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read(configPath)

    # get some http info from file :config.ini
    def get_http(self, name):
        return self.config.get("HTTP", name)

    def get_email(self, name):
        return self.config.get("EMAIL", name)