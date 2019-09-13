#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
UserScore.py
Authors: rensike(rensike@baidu.com)
Date:    2019/9/13 下午12:21
"""

from py_peewee.db import BaseModel
from peewee import IntegerField,CharField,DateTimeField

class UserScore(BaseModel):
    class Meta:
        table_name = "uscore"

    id = IntegerField(primary_key=True)
    name = CharField()
    uid = IntegerField(column_name="uid")
    create_at = DateTimeField()

