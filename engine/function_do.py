#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/7 9:49
# @Author  : lczean
# @File    : function_do.py

def sayhi():
    name = raw_input('Enter your name:')
    print '\033[36mHello %s\033[0m' % name
sayhi()
