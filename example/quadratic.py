#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-03 10:55:01
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : quadratic.py


# 二次方程式 ax**2 + bx + c = 0
# a b c 用户提供

# 导入cmath（复杂数学运算模块）
import cmath

a = float(input('输入 a：'))
b = float(input('输入 b：'))
c = float(input('输入 c：'))

# 计算
d = (b**2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为：{0}和{1}'.format(sol1, sol2))
