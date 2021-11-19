#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
封装driver
"""

import json
from appium import webdriver
from Baseic.Path import yaml_path
from Baseic.access_yaml import shopkeeper


# 初始化driver
def shopkeeper_driver():
    desired_caps = shopkeeper(yaml_path)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    # driver.launch_app()
    # driver.implicitly_wait(8)
    return driver
