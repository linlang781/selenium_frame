import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from utils.SeleniumExt import SeleniumExt
from utils.SikuliLib import SikuliLib
from pageobject.login import LoginPage

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.driver = SeleniumExt('chrome')
        self.driver.get('http://bj.tuanche.com/brand/')
        self.driver.wait(5)
        self.screen = SikuliLib()
    def tearDown(self):
        pass

    def test_new_car(self):
        new_car_url = self.driver.current_url
        pinpai = self.driver.element('id', 'factoryVal')
        self.driver.select_by_value(pinpai,'50')
        style = self.driver.element('xpath', '//*[@id="sideForm"]/div[2]/select')
        if not style:
            print(10)
        self.driver.select_by_value(style, '32268')
        phone = self.driver.element('name', 'phone')
        phone.send_keys('15602236699')
        btn = self.driver.element('class', 'inputsubmit-sign')
        self.driver.click(btn)
        car_url = self.driver.current_url
        if new_car_url != car_url:
            pass


    # def test_login(self):
    #     self.driver.login('admin','Admin999')
    #     time.sleep(100)
    # def test_order(self):
    #     web_form = self.driver.element('xpath', '/html/body/div[1]/div[1]/div/div/form')
    #     city_input_ele = web_form.find_element_by_class_name('festival')
    #     carType_ele = web_form.find_element_by_class_name('festiva2')
    #     citydlfirst = self.driver.element('id','citydlfirst')
    #     carType = self.driver.element('id','carType')
    #     commit_btn_ele = self.driver.element('xpath','/html/body/div[1]/div[1]/div/div/form/div[5]')
    #     try:
    #         if name_input_ele and phone_input_ele and city_input_ele and carType_ele:
    #             name_input_ele.send_keys('name')
    #             phone_input_ele.send_keys('15510478414')
    #             city_input_ele.click()
    #             if not citydlfirst:
    #                 self.fail('点击城市表单，没有弹出下拉框')
    #             city_input_ele.click()
    #             city_input_ele.send_keys(u'江阴   惠民车展')
    #             time.sleep(5)
    #             carType_ele.click()
    #             if not carType:
    #                 self.fail('点击车型，没有弹窗')
    #             carType_ele.click()
    #             carType_ele.send_keys(u'宝骏 - 宝骏310W')
    #             commit_btn_ele.click()
    #             time.sleep(20)
    #     except NoSuchElementException as e:
    #         print(e)


if __name__ == '__main__':
    unittest.main()
    # inspect.stack()[1][3]