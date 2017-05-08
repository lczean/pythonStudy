#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-08 14:58:49
# @Author  : lczean (lczean@163.com)
# @Link    : https://github.com/lczean
# @Version : 1.0
# @File    : hellocgi.py

'''
# CGI测试
'''

print("Content-type:text/html")
print()                             # 空行，告诉服务器结束头部
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>Hello Word - 我的第一个 CGI 程序！</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! 我是来自W3Cschool教程的第一CGI程序</h2>')
print('</body>')
print('</html>')
