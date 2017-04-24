#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/7 9:55
# @Author  : lczean
# @File    : function_do2.py

def sayhi():
    name = raw_input('Enter your name:')
    print '\033[36mHello %s\033[0m' % name
    if name == "ninghua":
        print 'ninghua age is old boy'
    else:
        print "our's works is IT"
sayhi()