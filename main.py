#!/usr/bin/env python
# encoding: utf-8
from utils.log import Logger
import unittest, time
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from utils.config import REPORT_PATH
logger=Logger().get_logger()
test_dir = './test/case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_file_name = './report/' + now + 'result.html'
    fp = open(report_file_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title='接口自动化测试报告', description='用例执行情况如下')
    runner.run(discover)
    fp.close()
    to_list = ['liuyu01@fengmap.com']
    cc_list = ['liuyu01@fengmap.com']
    file_path_tuple = (report_file_name,)
    email_username = ConfigOperate().get_config('email', 'username')
    email_passwd = ConfigOperate().get_config('email', 'passwd')
    email_smtp = ConfigOperate().get_config('email', 'smtp')
    send_conf = Email(email_smtp, email_username, email_passwd)
    if send_conf.send_email(to_list, cc_list, sub='接口测试报告' + now, content=open(report_file_name, 'rb').read(), file_path=file_path_tuple):   # content=open(report_file_name, 'rb').read()
        print('发送成功')
    else:
        print('发送失败')

