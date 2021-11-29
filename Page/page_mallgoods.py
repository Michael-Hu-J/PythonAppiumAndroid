#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from Basic.base import Base


class MallGoods(Base):
    def add_goods(self):
        self.swipe_find_element(element_locate="//android.widget.TextView[@text='商品管理']").click()
        self.click_element(element_locate="//android.widget.TextView[@text='分类管理']", page_description="点击分类管理")
        self.click_element(element_locate="//android.widget.TextView[@text='商品分类']", page_description="点击添加商品分类")

        # 混合定位，两个属性值均属于同一个元素
        self.find_element_android_uiautomator(
            ui_selector='new UiSelector().resourceId("zmsoft.rest.phone:id/txtContent").text("必填")',
            page_description="点击编辑商品分类名称").click()
        self.find_element_android_uiautomator(
            ui_selector='new UiSelector().resourceId("zmsoft.rest.phone:id/txtContent").text("必填")',
            page_description="编辑商品分类名称").send_keys("自动化测试分类")
        # self.send_text(element_locate="//android.widget.EditText[@text='必填']", text="自动化测试分类", page_description="编辑商品分类名称")

        self.click_element(
            element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/text_right_str']",
            page_description="点击保存商品分类")
        self.click_element(
            element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/text_left_str']",
            page_description="点击关闭分类管理")
        self.click_element(element_locate="//android.widget.TextView[@text='商品信息']", page_description="点击商品信息")
        self.click_element(element_locate="//android.widget.TextView[@text='添加']", page_description="点击添加商品")
        self.click_element(
            element_locate="//android.widget.LinearLayout[@resource-id='zmsoft.rest.phone:id/layoutAddSelf']",
            page_description="点击手动添加")

        # 从商品分类节点定位到其父节点，然后再找到其父节点下第一个android.widget.ImageView元素
        # self.find_element_xpath(element_locate="//android.widget.TextView[@text='商品分类']/../android.widget.ImageView[1]").click()

        """按特定的值选择商品分类"""
        text = "test"
        while text != "自动化测试分类":
            # 通过商品分类元素定位到同一父级下的兄弟元素zmsoft.rest.phone:id/detail
            self.find_element_android_uiautomator(
                ui_selector='new UiSelector().text("商品分类").fromParent(resourceId("zmsoft.rest.phone:id/detail"))',
                page_description="点击商品分类下拉").click()
            # 一次刚好滑动一个分类
            self.swipe(start_x=0.5, start_y=0.8, end_x=0.5, end_y=0.77, duration=500)
            self.click_element(
                element_locate="//android.widget.TextView[@resource-id='zmsoft.rest.phone:id/btn_confirm']",
                page_description="点击确认商品分类")
            # 获取商品分类当前已选择的分类名称
            text = self.find_element_android_uiautomator(
                ui_selector='new UiSelector().text("商品分类").fromParent(resourceId("zmsoft.rest.phone:id/detail"))',
                page_description="点击商品分类下拉").text

        self.find_element_android_uiautomator(
            ui_selector='new UiSelector().text("商品名称").fromParent(resourceId("zmsoft.rest.phone:id/detail"))',
            page_description="编辑商品名称").send_keys("自动化测试商品")
        self.click_element(element_locate="//android.widget.TextView[@text='保存']", page_description="点击保存商品")

    def delete_goods(self):
        self.swipe_find_element(element_locate="//android.widget.TextView[@text='商品管理']").click()
        self.click_element(element_locate="//android.widget.TextView[@text='商品信息']", page_description="点击商品信息")
        self.click_element(element_locate="//android.widget.TextView[@text='自动化测试商品']", page_description="点击商品")

        # 判断是否滑动到底部，删除按钮在底部
        before_swipe = "before"
        after_swipe = "after"
        while before_swipe != after_swipe:
            """判断是否滑动到屏幕底部"""
            before_swipe = self.driver.page_source
            self.swipe_up()
            after_swipe = self.driver.page_source

        self.click_element(element_locate="//android.widget.TextView[@text='删除']", page_description="点击删除商品")
        self.click_element(element_locate="//android.widget.Button[@text='确定']", page_description="点击确定删除商品")
        self.click_element(
            element_locate="//android.widget.LinearLayout[@resource-id='zmsoft.rest.phone:id/layout_left']",
            page_description="点击返回到商品管理页")
        self.click_element(element_locate="//android.widget.TextView[@text='分类管理']", page_description="点击分类管理")
        self.click_element(element_locate="//android.widget.TextView[@text='自动化测试分类']", page_description="点击商品分类")
        self.click_element(element_locate="//android.widget.TextView[@text='删除']", page_description="点击删除商品分类")
        self.click_element(element_locate="//android.widget.Button[@text='确定']", page_description="点击确定删除商品分类")
