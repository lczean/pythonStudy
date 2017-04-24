#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/7 9:27
# @Author  : lczean
# @File    : for_fo.py

for i in range(1, 10):
    # print i
    print '\033[35mThe number is %s \033[0m' % i
else:
    print 'The loop is exec done!'