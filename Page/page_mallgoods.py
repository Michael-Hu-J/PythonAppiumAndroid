#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from Basic.base import Base


class MallGoods(Base):
    def add_goods(self):
        # time.sleep(8)
        self.swipe_find_element(element_locate="//android.widget.TextView[@text='商品管理']").click()
        self.click_element(element_locate="//android.widget.TextView[@text='分类管理']", page_description="点击分类管理")
        self.click_element(element_locate="//android.widget.TextView[@text='商品分类']", page_description="点击添加商品分类")
        self.send_text(element_locate="//android.widget.EditText[@text='必填']", text="自动化测试分类", page_description="编辑商品分类名称")
        self.click_element(element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/text_right_str']", page_description="点击保存商品分类")
        self.click_element(element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/text_left_str']", page_description="点击关闭分类管理")
        self.click_element(element_locate="//android.widget.TextView[@text='商品信息']", page_description="点击商品信息")
        self.click_element(element_locate="//android.widget.TextView[@text='添加']", page_description="点击添加商品")
        self.click_element(element_locate="//android.widget.ImageView[@resource-id='zmsoft.rest.phone:id/ivSelfAdd']", page_description="点击手动添加商品")
        self.find_element_xpath(element_locate="//android.widget.TextView[@text='商品分类']..[3]").click()

