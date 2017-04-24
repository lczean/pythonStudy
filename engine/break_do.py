#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/7 9:33
# @Author  : lczean
# @File    : break_do.py

while True:
    A = raw_input('Enter a number: ')
    if A == '23':
        print "The number is %s !" % A
        break
    else:
        print "you get %s, Please continue enter number." % A