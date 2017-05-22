#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 16:02:36
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Filename: re.py


import re
from urllib.request import urlopen
from urllib.parse import quote


#\d*？ 数字
#\s 空格
#\s+? 多个空格
#[\s\S]+? 不管空格中间是什么，全匹配
#\w+？ 字符串
#[\w\W] 分组
#[\w\W\s\S\d\D]+？
