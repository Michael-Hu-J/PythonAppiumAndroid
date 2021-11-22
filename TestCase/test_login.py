#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pytest
from Page.page_login import Login


@pytest.mark.usefixtures("init_driver")
class TestLogin:
    def test_login(self, init_driver):
        Login(init_driver).correct_login()
