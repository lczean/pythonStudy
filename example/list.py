#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-09 14:20:58
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : list.py

'''
# list 显示列表
# isinstance 内置函数 判断数据类型 返回True或False
'''

# list 列表从0开始，先进后出，属于堆栈
# MOVIES = ["肖申克的救赎", "霸王别姬", "大话西游"]
# MOVIES.insert(1, 1997)
# MOVIES.insert(3, 1993)
# MOVIES.append(1995)

MOVIES = ["肖申克的救赎", 1994, "弗兰克·德拉邦特", 142,
          ["蒂姆·罗宾斯",
           ["摩根·弗里曼", "鲍勃·冈顿", "威廉姆·塞德勒", "克兰西·布朗 & 吉尔·贝罗斯"]]]

# 遍历列表,中间使用if判断是否存在嵌套列表
# No.1
for each_item in MOVIES:
    print(each_item)
print("***************")
# No.2
for each_item in MOVIES:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
# No.3
print("***************")
for each_item in MOVIES:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for nested_item_2 in nested_item:
                    print(nested_item_2)
            else:
                print(nested_item)
    else:
        print(each_item)
