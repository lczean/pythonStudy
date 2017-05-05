#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-05 16:41:03
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : match.py

'''
# 正则表达式匹配
# group(num=0)    匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''

import re
# 在起始位置匹配
print(re.match('www', 'www.baidu.com').span())
# 不在起始位置匹配
print(re.match('cn', 'www.baidu.com'))

LINE = "Cats are smarter than dogs"

macth_obj = re.match(r'(.*) are (.*?) .*', LINE, re.M |re.I)  # pylint: disable=C0103
if macth_obj:
    print("macth_obj.group(): ", macth_obj.group())
    print("macth_obj.group(1): ", macth_obj.group(1))
    print("macth_obj.group(2): ", macth_obj.group(2))
else:
    print("No match!!")
