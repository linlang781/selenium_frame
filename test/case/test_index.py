import time
import unittest
import random
from selenium import webdriver
from test.common.browser import Browser
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.driver = Browser('chrome')
        self.driver.get(Config().get('URL'))
    def tearDown(self):
        self.driver.quit()

    # def test_click_every_ele(self):
    #     ele = self.driver.find_elements(By.XPATH, '/html/body/div[2]/section[1]/div/div/div')
    #     print(len(ele))
    #     if ele:
    #         for i in ele:
    #             if i:
    #                 i.click()
    #                 print(self.driver.title)
    #                 time.sleep(10)
    #                 self.driver.back()
    #             else:
    #                 print('ele not find')
    #     else:
    #         print('ele is not find')




if __name__ == '__main__':
    unittest.main()