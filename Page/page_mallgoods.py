#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from Basic.base import Base

class MallGoods(Base):
    def add_goods(self):
        time.sleep(8)
        self.swipe_find_element(element_locate="//android.widget.TextView[@text='商品管理']").click()