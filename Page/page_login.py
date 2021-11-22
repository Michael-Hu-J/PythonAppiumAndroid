#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from Baseic.base import Base


class Login(Base):
    def correct_login(self):
        time.sleep(8)
        self.wait_element_explicit(
            element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']",
            page_description="输入正确手机号").send_keys(
            "17771432222")
        self.wait_element_explicit(
            element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etPassword']",
            page_description="输入正确密码").send_keys(
            "qa1234")
        self.wait_element_explicit(
            element_locate="//android.widget.Button[@resource-id='zmsoft.rest.phone:id/btnLogin']",
            page_description="点击登录").click()

    def err_username(self):
        time.sleep(8)
        self.wait_element_explicit(
            element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']",
            page_description="输入错误手机号").send_keys(
            "17771432223")
        self.wait_element_explicit(
            element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etPassword']",
            page_description="输入正确密码").send_keys(
            "qa1234")
        self.wait_element_explicit(
            element_locate="//android.widget.Button[@resource-id='zmsoft.rest.phone:id/btnLogin']",
            page_description="点击登录").click()
        warning = self.wait_element_explicit(
            element_locate="//android.widget.LinearLayout[@resource-id='zmsoft.rest.phone:id/parentPanel']",
            page_description="查找提示框").is_displayed()
        return warning

    def err_password(self):
        time.sleep(8)
        self.wait_element_explicit(
            element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etMobile']",
            page_description="输入错误手机号").send_keys(
            "17771432222")
        self.wait_element_explicit(
            element_locate="//android.widget.EditText[@resource-id='zmsoft.rest.phone:id/etPassword']",
            page_description="输入正确密码").send_keys(
            "qa12345")
        self.wait_element_explicit(
            element_locate="//android.widget.Button[@resource-id='zmsoft.rest.phone:id/btnLogin']",
            page_description="点击登录").click()
        warning = self.wait_element_explicit(
            element_locate="//android.widget.LinearLayout[@resource-id='zmsoft.rest.phone:id/parentPanel']",
            page_description="查找提示框").is_displayed()
        return warning

    def empty_input(self):
        time.sleep(8)
        self.wait_element_explicit(
            element_locate="//android.widget.Button[@resource-id='zmsoft.rest.phone:id/btnLogin']",
            page_description="点击登录").click()
