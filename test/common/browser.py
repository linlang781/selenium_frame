import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import * #导入所有的异常类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None
    # ----------------------浏览器操作--------------------
    def get(self, url, maximize_window=True, implicitly_wait=30):
        '''打开浏览器，目标URL在config.yml'''
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        '''截屏，保存目录为REPORT_PATH'''
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        '''关闭页面'''
        self.driver.close()

    def back(self):
        '''返回上级页面'''
        self.driver.back()

    def forward(self):
        '''前进'''
        self.driver.forward()

    def quit(self):
        '''退出浏览器'''
        self.driver.quit()

    def refresh(self):
        '''刷新页面'''
        self.driver.refresh()

    # ------------------窗口操作-------------------------
    @property
    def current_window(self):
        '''获取当前窗口句柄'''
        return self.driver.current_window_handle

    @property
    def title(self):
        '''获取当前页面标题'''
        return self.driver.title

    @property
    def current_url(self):
        '''获取当前页面url'''
        return self.driver.current_url

    def execute(self, js, *args):
        '''执行js语句'''
        self.driver.execute_script(js, *args)

    # -----------------定位元素---------------------------

    def find_element(self,*element):
        """
        重定义定位方法
        return self.driver.find_element(*element)
        """
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_element(*element)
        except:
            print("页面元素未能找到%s"%self,element)

    def find_elements(self,*element):
        """
        重定义定位方法
        return self.driver.find_element(*element)
        """
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_elements(*element)
        except:
            print("页面元素未能找到%s"%self,element)

    def find_element_by_id_wait(self, ele, sec=30):
        '''显式等待定位id'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_id(ele))

    def find_element_by_name_wait(self, ele, sec=30):
        '''显式等待定位name'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_name(ele))

    def find_element_by_xpath_wait(self, ele, sec=30):
        '''显式等待定位xpath'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_xpath(ele))

    def find_element_by_link_text_wait(self, ele, sec=30):
        '''显式等待定位link_text'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_link_text(ele))

    def find_element_by_partial_link_text_wait(self, ele, sec=30):
        '''显式等待定位partial_link_text'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_partial_link_text(ele))

    def find_element_by_tag_name_wait(self, ele, sec=30):
        '''显式等待定位tag_name'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_tag_name(ele))

    def find_element_by_class_name_wait(self, ele, sec=30):
        '''显式等待定位class_name'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_class_name(ele))

    def find_element_by_css_selector_wait(self, ele, sec=30):
        '''显式等待定位css_selector'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_element_by_css_selector(ele))

    def find_elements_by_name_wait(self, ele, sec=30):
        '''显式等待定位names'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_name(ele))

    def find_elements_by_xpath_wait(self, ele, sec=30):
        '''显式等待定位xpaths'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_xpath(ele))

    def find_elements_by_link_text_wait(self, ele, sec=30):
        '''显式等待定位link_texts'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_link_text(ele))

    def find_elements_by_partial_link_text_wait(self, ele, sec=30):
        '''显式等待定位partial_link_texts'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_partial_link_text(ele))

    def find_elements_by_tag_name_wait(self, ele, sec=30):
        '''显式等待定位tag_names'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_tag_name(ele))

    def find_elements_by_class_name_wait(self, ele, sec=30):
        '''显式等待定位class_names'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_class_name(ele))

    def find_elements_by_css_selector_wait(self, ele, sec=30):
        '''显式等待定位css_selectors'''
        return WebDriverWait(self.driver, sec).until(lambda x: x.find_elements_by_css_selector(ele))

    # ----------------------------元素操作---------------------------------
    def click(self, element):
        """点击操作"""
        element.click()

    def right_click(self, ele):
        '''右键'''
        ActionChains(self.driver).context_click(ele).perform()

    def double_click(self, ele):
        '''双击666'''
        ActionChains(self.driver).double_click(ele).perform()
        
    def send_keys(self, element, text):
        """发送文本"""
        element.clear()
        element.send_keys(text)

    def move_to_element(self, element):
        '''鼠标悬停'''
        ActionChains(self.driver).move_to_element(element).perform()

    def drag_and_drop(self, ele, target):
        '''拖拽元素'''
        ActionChains(self.driver).drag_and_drop(ele, target).perform()

    def get_text(self, element):
        '''获取文本'''
        return element.text

    def get_attribute(self, element, name):
        '''获取属性'''
        return element.get_attribute(name)

    def js_execute(self, js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self, element):
        '''聚焦元素'''
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, element, index):
        '''通过索引,index是索引第几个，从0开始'''
        element = self.find_element(element)
        Select(element).select_by_index(index)

    def select_by_value(self, element, value):
        '''通过value属性'''
        element = self.find_element(element)
        Select(element).select_by_value(value)

    def select_by_text(self, element, text):
        '''通过文本值定位'''
        element = self.find_element(element)
        Select(element).select_by_value(text)

    def is_text_in_element(self, element, text, timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(element, text))
        except TimeoutException:
            print("元素没有定位到:" + str(element))
            return False
        else:
            return result

    def is_text_in_value(self, element, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(element, value))
        except TimeoutException:
            print("元素没定位到：" + str(element))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''判断title完全等于'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''判断title包含'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, element, timeout=10):
        '''判断元素被选中，返回布尔值,'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(element))
        return result

    def is_selected_be(self, element, selected=True, timeout=10):
        '''判断元素的状态，selected是期望的参数true/False
        返回布尔值'''
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.element_located_selection_state_to_be(element, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, element, timeout=10):
        '''元素可见返回本身，不可见返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(element))
        return result

    def is_invisibility(self, element, timeout=10):
        '''元素可见返回本身，不可见返回True，没找到元素也返回True'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(element))
        return result

    def is_clickable(self, element, timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(element))
        return result

    def is_located(self, element, timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(element))
        return result

    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            print('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        print(self.driver.current_url, self.driver.title)

    def switch_to_frame(self, param):
        '''选择frame'''
        self.driver.switch_to.frame(param)

    def switch_to_alert(self):
        '''选择alert'''
        return self.driver.switch_to.alert
        #  t = self.driver.switch_to.alert
        # t.accept() 点击确认
        # t.dismiss（），点击x按钮取消

    def wait(self, sec):
        '''隐式等待'''
        self.driver.implicitly_wait(sec)



if __name__ == '__main__':
    b = Browser('chrome').get('http://www.baidu.com')
    b.save_screen_shot('test_baidu')
    time.sleep(3)
    b.quit()
