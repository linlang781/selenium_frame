#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuyu
@file: SikuliLib
@time: 2018/8/28
"""
from jpype import *
import traceback
import os

"""
调用sikuli方法，常用的click，exists，find，paste等方法
注：type和paste一些中文无法成功
"""

def SikuliLib():

    #用jpype调用sikuli-script.jar包，使用下面的命令加载
    #startJVM(jvm.dll路径,参数,jar包路径)

    try:
        jvmpath = r'C:\Program Files\Java\jdk1.8.0_181\jre\bin\server\jvm.dll'
        sikulipath = r'D:\sikuli1.1.1\sikulixapi.jar'
        print(sikulipath)
        if isJVMStarted() == False:
            startJVM(jvmpath,'-ea',r"-Djava.class.path={0}".format(sikulipath))
        else:
            pass
        #调用jar包的Screen类
        Screen = JClass('org.sikuli.script.Screen')
        #实例化类
        screen = Screen()
        return screen
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise AssertionError("ImSikuli--"+traceback.format_exc())

class SikuliExt(object):

    def __init__(self):
        self.screen = SikuliLib()

    def exists(self, imgObj):
        '''
        :param imgObj:判断图像是否存在
        :return: boolean
        '''
        return self.screen.exists(imgObj)

    def find(self, imgObj):
        '''
        查找匹配最佳的元素
        :param imgObj:
        :return:
        '''
        return self.screen.find(imgObj)

    def findAll(self, imgObj):
        '''
        查找全部元素
        :param imgObj:
        :return:
        '''
        return self.screen.findAll(imgObj)

    def click(self, imgObj, double = False):
        '''
        :param imgObj: 图片路径
        :param double: 是否双击
        :return:
        '''

        try:
            if double:
                self.screen.doubleClick(imgObj)
            else:
                self.screen.click(imgObj)
            return True
        except Exception as e:
            return e

    def rightClick(self, imgObj):
        '''
        右击
        :param imgObj: 图片路径
        :return:
        '''
        try:
            self.screen.rightClick(imgObj)
            return True
        except Exception as e:
            return e

    def wait(self, imgObj, wanish = False):
        '''
        等待GUI元素出现
        :param imgObj: 图片路径
        :return: boolean
        '''
        if wanish:
            return self.screen.waitVanish(imgObj)
        else:
            return self.screen.wait(imgObj)

    def hover(self, imgObj):

        self.screen.hover(imgObj)

    def dragDrop(self, imgObj, imgObjTarget):

        self.screen.drapDrop(imgObj, imgObjTarget)

    def type(self, text, imgObj=None):

        if imgObj is None:
            self.screen.type(text)
        else:
            self.screen.type(imgObj, text)

    def paste(self, text, imgObj=None):

        if imgObj is None:
            self.screen.paste(text)
        else:
            self.screen.paste(imgObj, text)

if __name__ == '__main__':
    pass



