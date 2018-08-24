import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH
from test.common.browser import Browser


class TestBaoming(unittest.TestCase):
    URL = Config().get('URL')
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        name_warp = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/form/div[1]')
        form_warp = self.driver.find_elements_by_class_name('formwrap')
        form_warp[1].send_keys('name')

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

