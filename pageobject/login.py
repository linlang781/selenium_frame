#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuyu
@file: login
@time: 2018/8/31
"""
from utils.SeleniumExt import SeleniumExt

class LoginPage(SeleniumExt):

    def login(self, loginname, lpasswd):
        username = self.element('id', 'empLogin')
        passwd = self.element('id', 'empPwd')
        clbtn = self.element('name', 'Submit')
        username.send_keys(loginname)
        passwd.send_keys(lpasswd)
        self.click(clbtn)




