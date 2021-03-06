#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
封装driver
"""

import time
from appium import webdriver
from Basic.Path import yaml_path
from Basic.yaml_data import shopkeeper


# 初始化driver
def shopkeeper_driver():
    desired_caps = shopkeeper(yaml_path)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    # driver.launch_app()
    return driver
