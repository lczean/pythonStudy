#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-10 09:48:25
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @File    : nester.py


'''这是"nester.py"模块，提供了一个名为print_lists的函数，这个函数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表。'''

# 模块 python标准库 PyPi
# 第三方python模块（Python Package Index,PyPl）
# Python包索引（Python Package Index,PyPl）为internet上的第三方Python模块提供了一个集中的存储库。
# 准备好之后，就可以使用PyPll来发布你的模块，从而使你的代码可供其他人使用。


def print_lists(the_list):
    '''
    这个函数取一个位置参数，名为"the_list"，
    这个可以是任何python列表，（也可以是包含嵌套列表的列表）。
    所指定的列表中的每个数据项（递归的）输出到屏幕上，各数据项个占一行。
    '''
    for each_items in the_list:
        if isinstance(each_items, list):# 判断是否是列表
            print_lists(each_items)  # 递归,python默认递归深度不能超过100个
        else:
            print(each_items)
