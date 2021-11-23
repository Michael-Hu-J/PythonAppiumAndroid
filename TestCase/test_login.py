#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pytest
from Page.page_login import Login


@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login(self, driver):
        warning = Login(driver).err_username()
        assert warning is True
