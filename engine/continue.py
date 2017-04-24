#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/7 9:38
# @Author  : lczean
# @File    : continue.py

while True:
    A = int(raw_input('Enter A number:'))
    if A == 23:
        print 'The number is %s !' % A
        break
    if A > 20:
        continue
        print '\033[34mPlease continue enter number.\033[0m'
print 'Done!'