#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
demo_update.py
Authors: rensike(rensike@baidu.com)
Date:    2019/9/13 下午12:52
"""

from py_peewee.models.user_score import UserScore

if __name__ == '__main__':
    # 查找ID=3的记录并进行更新
    uscore = UserScore.get(id=3)
    uscore.name = "myleilei"
    uscore.save()


