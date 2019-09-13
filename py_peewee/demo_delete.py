#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
demo_delete.py
Authors: rensike(rensike@baidu.com)
Date:    2019/9/13 下午12:54
"""

from py_peewee.models.user_score import UserScore

if __name__ == '__main__':
    # 插入一条新纪录并删除
    demo_uscore = UserScore.create(name="demo",uid=999)
    demo_uscore.delete_instance()
