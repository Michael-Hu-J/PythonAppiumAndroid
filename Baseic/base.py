#!/usr/bin/python3
# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Baseic.Log import MyLog


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 定义元素显示wait
    def wait_element_explicit(self, element_locate, page_description=None, wait_time=2):
        MyLog.info("正在{}：({})可见".format(page_description, element_locate))
        try:
            wait_element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, element_locate)))
            return wait_element
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            raise

    # 查找单个元素
    def find_element_xpath(self, element_locate, page_description=None):
        MyLog.info("正在{}：{}".format(page_description, element_locate))
        try:
            ele = self.driver.find_element_by_xpath(element_locate)
            return ele
        except Exception as err:
            MyLog.exception("{}失败：{]".format(page_description, err))
            raise

    # 查找多个元素
    def find_elements_xpath(self, element_locate, page_description=None):
        MyLog.info("正在{}：{}".format(page_description, element_locate))
        try:
            eles = self.driver.find_elements_by_xpath(element_locate)
            return eles
        except Exception as err:
            MyLog.exception("{}失败：{]".format(page_description, err))
            raise

    # 启动app
    def launch_app(self, page_description=None):
        MyLog.info("正在{}".format(page_description))
        try:
            self.driver.launch_app()
        except Exception as err:
            MyLog.info("{}失败！".format(page_description))
            raise

