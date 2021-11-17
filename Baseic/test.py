#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json
import os
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Baseic.driver import shopkeeper_driver
from base import Base


class Login(Base):
    # def __init__(self, driver):
    #     self.driver = driver


    def login(self):
        # username = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']"))
        # )
        # username = self.wait_element_explicit(element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']", page_description="等待元素")
        # # username = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']")
        # username.send_keys("17771432222")
        # password = self.driver.find_element_by_xpath(
        #     "//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etPassword']")
        # password.send_keys("qa1234")
        # self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='zmsoft.rest.phone:id/btnLogin']").click()
        # self.send_text(element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']", text="17771432624", page_description="输入账号")
        text = self.get_attribute(element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']", attribute_name="resource-id")
        print(text)
        self.get_screenshot(page_description="获取元素属性")



if __name__ == '__main__':
    os.system("adb connect 127.0.0.1:5555")
    driver = shopkeeper_driver()
    Login(driver).login()
    os.system("adb disconnect 127.0.0.1:5555")
