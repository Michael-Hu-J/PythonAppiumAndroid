#!/usr/bin/python3
# -*- coding:utf-8 -*-
import yaml


# 读取掌柜配置信息
def shopkeeper(yaml_path):
    with open(yaml_path, encoding="utf-8") as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)  # 编码成python对象
        desired_caps = data[0]["desired_caps_shopkeeper"]
        return desired_caps
