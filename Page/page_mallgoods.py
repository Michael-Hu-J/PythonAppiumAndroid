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

        # 混合定位，两个属性值均属于同一个元素
        self.find_element_android_uiautomator(
            ui_selector='new UiSelector().resourceId("zmsoft.rest.phone:id/txtContent").text("必填")',
            page_description="点击编辑商品分类名称").click()
        self.find_element_android_uiautomator(
            ui_selector='new UiSelector().resourceId("zmsoft.rest.phone:id/txtContent").text("必填")',
            page_description="编辑商品分类名称").send_keys("自动化测试分类6")
        # self.send_text(element_locate="//android.widget.EditText[@text='必填']", text="自动化测试分类", page_description="编辑商品分类名称")

        self.click_element(
            element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/text_right_str']",
            page_description="点击保存商品分类")
        self.click_element(
            element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/text_left_str']",
            page_description="点击关闭分类管理")
        self.click_element(element_locate="//android.widget.TextView[@text='商品信息']", page_description="点击商品信息")
        self.click_element(element_locate="//android.widget.TextView[@text='添加']", page_description="点击添加商品")
        self.click_element(element_locate="//android.widget.ImageView[@resource-id='zmsoft.rest.phone:id/ivSelfAdd']",
                           page_description="点击手动添加商品")

        # 从商品分类节点定位到其父节点，然后再找到其父节点下第一个android.widget.ImageView元素
        # self.find_element_xpath(element_locate="//android.widget.TextView[@text='商品分类']/../android.widget.ImageView[1]").click()

        # 通过商品分类元素定位到同一父级下的兄弟元素zmsoft.rest.phone:id/arrow
        self.find_element_android_uiautomator(
            ui_selector='new UiSelector().text("商品分类").fromParent(resourceId("zmsoft.rest.phone:id/arrow"))',
            page_description="点击商品分类下拉").click()
