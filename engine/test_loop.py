#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/6 15:03
# @Author  : lczean
# @File    : test_loop.py

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1

print "Good bye!"