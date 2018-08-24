import time
import unittest
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from test.common.browser import Browser
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.driver = Browser('chrome')
        self.driver.get(Config().get('New_car_url'))
        self.driver.wait(5)
    def tearDown(self):
        pass

    def test_order(self):
        name_input_ele = self.driver.find_element_by_xpath_wait('/html/body/div[1]/div[1]/div/div/form/div[1]/input')
        phone_input_ele = self.driver.find_element_by_xpath_wait('/html/body/div[1]/div[1]/div/div/form/div[2]/input')
        city_input_ele = self.driver.find_element_by_xpath_wait('/html/body/div[1]/div[1]/div/div/form/div[3]/input')
        carType_ele = self.driver.find_element_by_xpath_wait('/html/body/div[1]/div[1]/div/div/form/div[4]/input')
        citydlfirst = self.driver.find_element_by_id_wait('citydlfirst')
        carType = self.driver.find_element_by_id_wait('carType')
        commit_btn_ele = self.driver.find_element_by_xpath_wait('/html/body/div[1]/div[1]/div/div/form/div[5]')
        try:
            if name_input_ele and phone_input_ele and city_input_ele and carType_ele:
                name_input_ele.send_keys('name')
                phone_input_ele.send_keys('15510478414')
                city_input_ele.click()
                if not citydlfirst:
                    self.fail('点击城市表单，没有弹出下拉框')
                city_input_ele.click()
                city_input_ele.send_keys(u'江阴   惠民车展')
                time.sleep(5)
                carType_ele.click()
                if not carType:
                    self.fail('点击车型，没有弹窗')
                carType_ele.click()
                carType_ele.send_keys(u'宝骏 - 宝骏310W')
                commit_btn_ele.click()
                time.sleep(20)
        except NoSuchElementException as e:
            print(e)

    def test_select_new_car(self):

        self.driver.select_by_value((By.ID, 'factoryVal'), '10')

if __name__ == '__main__':
    unittest.main()