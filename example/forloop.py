#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-05 10:17:36
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : forloop.py

'''
# 将99乘法表写入文件
'''

# 创建文件
with open("forloop.txt", "wt") as out_file:
    # for loop
    for i in range(1, 10):
        for j in range(1, i + 1):
            TEXT = '{}x{}={}\t'.format(j, i, i * j)
            print(TEXT, end="")
            out_file.write(TEXT)
            if j == i:
                out_file.write("\n")
        print()


# 手动输入两个数字 显示其乘法表
I = int(input("input the first number: "))
# 创建文件forloop2.txt
with open("forloop1.txt", "wt") as new_out_file:
    # for loop
    for k in range(1, I + 1):
        for l in range(1, k + 1):
            TEXT2 = '{}x{}={}\t'.format(l, k, k * l)
            new_out_file.write(TEXT2)
            if k == l:
                new_out_file.write("\n")
        print()
