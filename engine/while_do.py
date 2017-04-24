#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/7 9:14
# @Author  : lczean
# @File    : while_do.py

b = 20
running = True
print '\033[32m==========================\033[0m'
while running:
    a = int(raw_input('Enter A number a: '))
    if a == b:
        print '\033[36mgood, a is %s equal b is %s !\033[0m' % (a, b)
        running = False  # stop
    elif a <b :
        print '\033[32mNo, it is a: %s little b: %s !\033[0m' % (a, b)
    else:
        print '\033[32mNo,it is a greater b !\033[0m'
else:
    print 'The loop is done !'
