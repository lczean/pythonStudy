#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 15:59:54
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : is_number.py


# 判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

#检测字符串和数字
print(is_number('foo'))     #False
print(is_number('1'))       #True
print(is_number('1.3'))     #True
print(is_number('-1.37'))       #True
print(is_number('1e3'))     #True

#测试Unicode
# 阿拉伯语 5
print(is_number('٥'))  # False
# 泰语 2
print(is_number('๒'))  # False
# 中文数字
print(is_number('四')) # False
# 版权号
print(is_number('©'))  # False