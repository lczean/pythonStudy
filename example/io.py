#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-05 10:06:22
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : io.py

'''
# 文件IO
'''

# write a file
with open("text.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\nJust a test!")

# read a file
with open("text.txt", "rt") as in_file:
    TEXT = in_file.read()

print(TEXT)
