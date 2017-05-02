#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-02 15:27:26
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0


# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0}和 {1}相加结果为：{2}'.format(num1, num2, sum))



# No.2

print('两数之和为%.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))