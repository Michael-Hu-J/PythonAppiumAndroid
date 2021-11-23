#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from Basic.base import Base


class Login(Base):
    def correct_login(self):
        """输入正确的手机号和密码登录"""
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
        avatar = self.wait_element_explicit(
            element_locate="//android.widget.ImageView[@resource-id='zmsoft.rest.phone:id/iv_avatar']",
            page_description="查找头像").is_displayed()
        return avatar

    def err_username(self):
        """输入错误的手机号码和正确的密码登录"""
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
        """输入正确的手机号码和错误的密码"""
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
        """不输入手机号码和密码登录"""
        time.sleep(8)
        self.wait_element_explicit(
            element_locate="//android.widget.Button[@resource-id='zmsoft.rest.phone:id/btnLogin']",
            page_description="点击登录").click()
        warning = self.get_text(
            element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/tv_message_dialog']",
            page_description="获取为空时提示内容")
        return warning
