import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.config import DRIVER_PATH, IMG_PATH
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import * #导入所有的异常类

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

class SeleniumExt(object):
    def __init__(self, type=None, mobile=False):
            if type == 'chrome':
                if not mobile:
                    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
                    options = webdriver.ChromeOptions()
                    options.add_experimental_option('mobileEmulation', mobileEmulation)
                    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
                else:
                    self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
            elif type == 'firefox':
                self.driver = webdriver.Firefox()
            elif type == 'ie':
                self.driver = webdriver.Ie(executable_path=IEDRIVER_PATH)
            elif type == 'phantomjs':
                self.driver = webdriver.PhantomJS(executable_path=PHANTOMJSDRIVER_PATH)
            else:
                raise NameError('只能输入firefox,ie,chrome,phantomjs')

    # ----------------------浏览器操作--------------------
    def get(self, url, maximize_window=True, implicitly_wait=30):
        '''打开浏览器，目标URL在config.yml'''
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)

    def save_screen_shot(self, name='screen_shot'):
        '''截屏，保存目录为IMG_PATH'''
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = IMG_PATH + '\screenshot_%s' % day
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

    def element(self, method, ele):  # 定位
        if method == 'id':
            element = self.driver.find_element_by_id(ele)
        elif method == "name":
            element = self.driver.find_element_by_name(ele)
        elif method == "class":
            element = self.driver.find_element_by_class_name(ele)
        elif method == "link_text":
            element = self.driver.find_element_by_link_text(ele)
        elif method == "xpath":
            element = self.driver.find_element_by_xpath(ele)
        elif method == "tag":
            element = self.driver.find_element_by_tag_name(ele)
        elif method == "css":
            element = self.driver.find_element_by_css_selector(ele)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element
    def elements(self, method, ele):  # 定位
        if method == 'id':
            element = self.driver.find_elements_by_id(ele)
        elif method == "name":
            element = self.driver.find_elements_by_name(ele)
        elif method == "class":
            element = self.driver.find_elements_by_class_name(ele)
        elif method == "link_text":
            element = self.driver.find_elements_by_link_text(ele)
        elif method == "xpath":
            element = self.driver.find_elements_by_xpath(ele)
        elif method == "tag":
            element = self.driver.find_elements_by_tag_name(ele)
        elif method == "css":
            element = self.driver.find_elements_by_css_selector(ele)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def element_wait(self, method, ele, wati=10):  # 等待
        if method == "id":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.ID, ele)))
        elif method == "name":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.NAME, ele)))
        elif method == "class":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.CLASS_NAME, ele)))
        elif method == "link_text":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.LINK_TEXT, ele)))
        elif method == "xpath":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.XPATH, ele)))
        elif method == "css":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ele)))
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

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

    def js_remove_attribute(self, attribute, eleId, frame=None):
        '''
        :param attribute: 要删除的属性
        :param eleId: 要删除属性的元素ID
        :param frame: frame元素ID
        :return:
        '''
        if frame is not None:
            js = "window.document.getElementById('%s').contentWindow.document.getElementById('%s').removeAttribute('%s')" % (frame, eleId, attribute)
            self.driver.execute_script(js)
        else:
            js = "window.document.getElementById('%s').removeAttribute('%s')" % (eleId, attribute)
            self.driver.execute_script(js)

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
        Select(element).select_by_index(index)

    def select_by_value(self, element, value):
        '''通过value属性'''
        Select(element).select_by_value(value)

    def select_by_text(self, element, text):
        '''通过文本值定位'''
        Select(element).select_by_visible_text(text)

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
    pass
