#!/usr/bin/env python
# encoding: utf-8
from utils.log import LOG
import unittest, time
from utils.BSTestRunner import BSTestRunner
from utils.SendMail import SendEmail
from utils.config import REPORT_PATH, CASE_PATH
from utils.config import Config
from utils.log import LOG

config = Config()
report_title = config.get('report_conf')['report_title']
report_desc = config.get('report_conf')['report_desc']
mail_to_list = config.get('mail_send_conf')['send_to']
mail_to_cc = config.get('mail_send_conf')['send_cc']
mail_title = config.get('mail_send_conf')['mail_title']
email_username = config.get('mail_base_conf')['username']
email_passwd = config.get('mail_base_conf')['passwd']
email_smtp = config.get('mail_base_conf')['smtp']
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_file_name = REPORT_PATH + now + 'result.html'

def add_case(case_path=CASE_PATH, rule='test*.py'):
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule)
    return discover


def run_case(all_case):
    fp = open(report_file_name, 'wb')
    runner = BSTestRunner(stream=fp, title=report_title, description=report_desc)
    runner.run(all_case)
    fp.close()


def send_report_mail():
    file_path_tuple = (report_file_name,)
    send_conf = SendEmail(email_smtp, email_username, email_passwd)
    if send_conf.send_email(mail_to_list, mail_to_cc, sub=mail_title + now, content=open(report_file_name, 'rb').read(), file_path=file_path_tuple):   # content=open(report_file_name, 'rb').read()
        LOG.info('测试邮件发送成功，测试时间{0}'.format(now))
    else:
        LOG.info('测试邮件发送失败，测试时间{0}'.format(now))

if __name__ == '__main__':
    run_case(add_case())
    send_report_mail()




