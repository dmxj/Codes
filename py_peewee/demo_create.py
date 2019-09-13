#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
demo_create.py
Authors: rensike(rensike@baidu.com)
Date:    2019/9/13 下午12:31
"""
from datetime import datetime

from py_peewee.models.user_score import UserScore

if __name__ == '__main__':
    # 使用save()，返回插入的行数1
    uscore = UserScore(name="rensike",uid=300,create_at=datetime(year=1993,month=6,day=3,hour=7,minute=25,second=36))
    # 创建新纪录，返回插入的行数
    num = uscore.save()
    print("add uscore count : ",num)

    # 使用create()，返回插入的实例
    new_uscore = UserScore.create(name="menglei",uid=520,create_at=datetime(year=1992,month=9,day=1,hour=8,minute=36,second=36))

    print("create a new uscore, id=",new_uscore.id)

    print("update and save new_usore")
    new_uscore.name = "zhangmenglei"
    new_uscore.save()
