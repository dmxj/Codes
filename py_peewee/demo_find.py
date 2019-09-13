#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
demo_find.py
Authors: rensike(rensike@baidu.com)
Date:    2019/9/13 下午12:30
"""

from py_peewee.models.user_score import UserScore

if __name__ == '__main__':
    # 条件查询，单条记录
    uscore0 = UserScore.get(UserScore.name=="rensike")
    print("find uscore0 where name=rensike, result is:",uscore0.name,"\t",uscore0.uid,"\t",uscore0.create_at)

    # 条件查询，多条记录
    uscore_list = UserScore.select().where(UserScore.uid >= 300)
    print("find uscore list where uid>=300")
    for u in uscore_list:
        print("uscore item for uscore_list is:",u.name)

    # 排序，或查询
    uscore_list1 = UserScore.select().where((UserScore.uid <= 200) | (UserScore.uid > 500)).order_by(UserScore.uid.desc())
    print("find uscore list where uid<=300 or uid>500")
    for u in uscore_list1:
        print("uscore name item for uscore_list1 is:", u.name)
