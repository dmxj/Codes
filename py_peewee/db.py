#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
db.py
Authors: rensike(rensike@baidu.com)
Date:    2019/9/13 下午12:19
"""

from peewee import MySQLDatabase, Model

db = MySQLDatabase("hello", host="127.0.0.1", port=3306, user="root", passwd="root")
db.connect()
print("database is connected.")

class BaseModel(Model):
    class Meta:
        database = db
