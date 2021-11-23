#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pytest
from Page.page_login import Login


@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_correct_login(self, driver):
        avatar = Login(driver).correct_login()
        assert avatar is True

    def test_err_username_login(self, driver):
        warning = Login(driver).err_username()
        assert warning is True

    def test_err_password_login(self, driver):
        warning = Login(driver).err_password()
        assert warning is True

    def test_empty_input_login(self, driver):
        warning = Login(driver).empty_input()
        assert warning == "手机号码不能为空!"
