# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2020/12/3
@Description: 配置文件
"""
import os


class Config(object):
    def __init__(self):
        self.project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
