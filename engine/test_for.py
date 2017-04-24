#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/4/5 15:42
# @Author  : lczean
# @File    : test_for.py

# for letter in 'Python':  # 第一个实例Python
#     print '当前字母 :', letter
#
# fruits = ['banana', 'apple', 'mango']  # 第二个实例
# for fruit in fruits:
#     print '当前水果：', fruit
#
# print "The End"
#
# # 通过序列索引迭代
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print '当前水果：', fruits[index]


# for num in range(10, 20):    # 迭代 10 到 20 之间的数字
#     for i in range(2, num):  # 根据因子迭代
#         if num % i == 0:     # 确定第一个因子
#             print 'num =', num, 'i =', i
#             j = num / i      # 计算第二个因子
#             print '%d 等于 %d * %d ' % (num, i, j)
#             break            # 跳出当前循环
#         else:                # 循环的else部分
#             print num, '是一个质数'
#             print 'num =', num, 'i =', i
