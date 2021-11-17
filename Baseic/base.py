#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os.path
import time
from Baseic.Path import base_dir
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Baseic.Log import MyLog


class Base:
    def __init__(self, driver):
        self.driver = driver

    """
   :param element_locate: 元素的xpath定位
   :param page_description: 行为描述
   :param attribute_name：属性名
    """

    # 定义元素显示wait
    def wait_element_explicit(self, element_locate, page_description=None, wait_time=5):
        MyLog.info("正在{}：({})可见".format(page_description, element_locate))
        try:
            wait_element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, element_locate)))
            return wait_element
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 启动app
    def launch_app(self, page_description=None):
        MyLog.info("正在{}".format(page_description))
        try:
            self.driver.launch_app()
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 查找单个元素
    def find_element_xpath(self, element_locate, page_description=None):
        MyLog.info("正在{}：({})".format(page_description, element_locate))
        try:
            ele = self.driver.find_element_by_xpath(element_locate)
            return ele
        except Exception as err:
            MyLog.exception("{}失败：{]".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 查找多个元素
    def find_elements_xpath(self, element_locate, page_description=None):
        MyLog.info("正在{}：({})".format(page_description, element_locate))
        try:
            eles = self.driver.find_elements_by_xpath(element_locate)
            return eles
        except Exception as err:
            MyLog.exception("{}失败：{]".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 输入文本
    def send_text(self, element_locate, text, page_description=None):
        ele = self.wait_element_explicit(element_locate, page_description="等待元素")
        MyLog.info("正在{}：{}".format(page_description, text))
        try:
            ele.clear()
            ele.send_keys(text)
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 获取元素文本
    def get_text(self, element_locate, page_description=None):
        ele = self.wait_element_explicit(element_locate, page_description="等待元素")
        try:
            text = ele.text
            MyLog.info("已成功{}：{}".format(page_description, text))
            return text
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            raise

    # 获取元素属性
    def get_attribute(self, element_locate, attribute_name):
        ele = self.wait_element_explicit(element_locate, page_description="等待元素")
        try:
            att = ele.get_attribute(attribute_name)
            MyLog.info('已成功获取"{}"元素属性'.format(attribute_name))
            return att
        except Exception as err:
            MyLog.exception('获取"{}"元素失败：{}'.format(attribute_name, err))

    # 屏幕截图
    def get_screenshot(self, page_description=None):
        screenshot_path = os.path.join(base_dir, "screenshots/{}_{}.png".format(page_description,
                                                                                time.strftime("%Y-%m-%d",
                                                                                              time.localtime())))
        self.driver.get_screenshot_as_file(screenshot_path)
        MyLog.info("错误截图保存在 ")
