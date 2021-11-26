#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pytest
from Page.page_mallgoods import MallGoods


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("launch_app")
class TestMallGoods:
    def test_add_goods(self, driver):
        MallGoods(driver).add_goods()
