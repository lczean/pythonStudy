#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 15:18:28
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Filename: readfile.py


# 读取文件，以‘:’为分隔符
data = open('sketch.txt')
for each_line in data:
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said：', end='')
        print(line_spoken, end='')
data.seek(0)
data.close()


# try/except机制
data = open('sketch.txt')
for each_lines in data:
    try:
        (roles, line_spokens) = each_lines.split(':', 1)
        print(roles, end='')
        print(' said：', end='')
        print(line_spokens, end='')
    except:
        pass
data.seek(0)
data.close()
