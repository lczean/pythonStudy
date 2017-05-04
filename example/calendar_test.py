#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 16:51:21
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : calendar_test.py

'''
# add docstring 说明
# set the variables：
    1.year：YY
    2.mouth: MM
'''

# 引人日历模块
import calendar

# 输入指定年月，常量必须大写，否则违法命名规范
YY = int(input('输入年份：'))
MM = int(input('输入月份：'))

# 显示日历
print(calendar.month(YY, MM))
