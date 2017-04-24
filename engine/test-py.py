#!/usr/bin/python
# coding=utf-8
# 文件名：test-py.py

#test1
print "test1";

#test2
if True:
    print "Answer"
    print "test2 True"
else:
    print "Answer"
    print "test2 False"

#test3
word = 'word'
sentence = "这是一个句子。"
paragraph = """test3 这是一个段落。
包含了多个语句"""
print paragraph

#test4
#raw_input("\n\nPress the enter key to exit.")

#test5
import sys; x='test5'; sys.stdout.write(x+'\n')

#test6
x="a"
y="b"
#换行输出
print x
print y
print '============'
#不换行输出
print x,
print y,

print '\n'
#test7
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name


#test8
a=b=c=1
print a==b
print a==c

a,b,c=1,2,"john"
print a
print b
print c

#test9
str = 'Hello World!'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

#test10 列表
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

#test11 元组 不能二次赋值，相当于只读列表
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组


#test12
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

#test13

num =10
if num <0 or num > 10:
    print 'hello'
else:
    print 'underfine'
