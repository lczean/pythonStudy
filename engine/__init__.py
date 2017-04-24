#!/usr/bin/python
# -*- coding:UTF-8 -*-

print "测试项目，Python!";


# pycharm 自动添加注释
# File->settings->Editor->File and Code Templates->Python Script
# 添加以下代码

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : ${DATE} ${TIME}
# @Author  : otfsenter
# @File    : ${NAME}.py



# Alt+Enter 自动添加包
# shift+O 自动建议代码补全
# Ctrl+t SVN更新
# Ctrl+k SVN提交
# Ctrl + / 注释(取消注释)选择的行
# Ctrl+Shift+F 高级查找
# Ctrl+Enter 补全
# Shift + Enter 开始新行
# TAB Shift+TAB 缩进/取消缩进所选择的行
# Ctrl + Alt + I 自动缩进行
# Ctrl + Y 删除当前插入符所在的行
# Ctrl + D 复制当前行、或者选择的块
# Ctrl + Shift + J 合并行
# Ctrl + Shift + V 从最近的缓存区里粘贴
# Ctrl + Delete 删除到字符结尾
# Ctrl + Backspace 删除到字符的开始
# Ctrl + NumPad+/- 展开或者收缩代码块
# Ctrl + Shift + NumPad+ 展开所有的代码块
# Ctrl + Shift + NumPad- 收缩所有的代码块
#
# http://blog.csdn.NET/pipisorry/article/details/39909057
#
# 在PyCharm /opt/pycharm-3.4.1/help目录下可以找到ReferenceCard.pdf快捷键英文版说明
#
# PyCharm Default Keymap
# PyCharm3.0默认快捷键(翻译的)
#
# 1、编辑（Editing）
# Ctrl + Space 基本的代码完成（类、方法、属性）
# Ctrl + Alt + Space 快速导入任意类
# Ctrl + Shift + Enter 语句完成
# Ctrl + P 参数信息（在方法中调用参数）
# Ctrl + Q 快速查看文档
# Shift + F1 外部文档
# Ctrl + 鼠标 简介
# Ctrl + F1 显示错误描述或警告信息
# Alt + Insert 自动生成代码
# Ctrl + O 重新方法
# Ctrl + Alt + T 选中
# Ctrl + / 行注释
# Ctrl + Shift + / 块注释
# Ctrl + W 选中增加的代码块
# Ctrl + Shift + W 回到之前状态
# Ctrl + Shift + ]/[ 选定代码块结束、开始
# Alt + Enter 快速修正
# Ctrl + Alt + L 代码格式化
# Ctrl + Alt + O 优化导入
# Ctrl + Alt + I 自动缩进
# Tab / Shift + Tab 缩进、不缩进当前行
# Ctrl+X/Shift+Delete 剪切当前行或选定的代码块到剪贴板
# Ctrl+C/Ctrl+Insert 复制当前行或选定的代码块到剪贴板
# Ctrl+V/Shift+Insert 从剪贴板粘贴
# Ctrl + Shift + V 从最近的缓冲区粘贴
# Ctrl + D 复制选定的区域或行
# Ctrl + Y 删除选定的行
# Ctrl + Shift + J 添加智能线
# Ctrl + Enter 智能线切割
# Shift + Enter 另起一行
# Ctrl + Shift + U 在选定的区域或代码块间切换
# Ctrl + Delete 删除到字符结束
# Ctrl + Backspace 删除到字符开始
# Ctrl + Numpad+/- 展开折叠代码块
# Ctrl + Numpad+ 全部展开
# Ctrl + Numpad- 全部折叠
# Ctrl + F4 关闭运行的选项卡
#
# 2、查找/替换(Search/Replace)
# F3 下一个
# Shift + F3 前一个
# Ctrl + R 替换
# Ctrl + Shift + F 全局查找
# Ctrl + Shift + R 全局替换
#
# 3、运行(Running)
# Alt + Shift + F10 运行模式配置
# Alt + Shift + F9 调试模式配置
# Shift + F10 运行
# Shift + F9 调试
# Ctrl + Shift + F10 运行编辑器配置
# Ctrl + Alt + R 运行manage.py任务
#
# 4、调试(Debugging)
# F8 跳过
# F7 进入
# Shift + F8 退出
# Alt + F9 运行游标
# Alt + F8 验证表达式
# Ctrl + Alt + F8 快速验证表达式
# F9 恢复程序
# Ctrl + F8 断点开关
# Ctrl + Shift + F8 查看断点
#
# 5、导航(Navigation)
# Ctrl + N 跳转到类
# Ctrl + Shift + N 跳转到符号
# Alt + Right/Left 跳转到下一个、前一个编辑的选项卡
# F12 回到先前的工具窗口
# Esc 从工具窗口回到编辑窗口
# Shift + Esc 隐藏运行的、最近运行的窗口
# Ctrl + Shift + F4 关闭主动运行的选项卡
# Ctrl + G 查看当前行号、字符号
# Ctrl + E 当前文件弹出
# Ctrl+Alt+Left/Right 后退、前进
# Ctrl+Shift+Backspace 导航到最近编辑区域
# Alt + F1 查找当前文件或标识
# Ctrl+B / Ctrl+Click 跳转到声明
# Ctrl + Alt + B 跳转到实现
# Ctrl + Shift + I查看快速定义
# Ctrl + Shift + B跳转到类型声明
# Ctrl + U跳转到父方法、父类
# Alt + Up/Down跳转到上一个、下一个方法
# Ctrl + ]/[跳转到代码块结束、开始
# Ctrl + F12弹出文件结构
# Ctrl + H类型层次结构
# Ctrl + Shift + H方法层次结构
# Ctrl + Alt + H调用层次结构
# F2 / Shift + F2下一条、前一条高亮的错误
# F4 / Ctrl + Enter编辑资源、查看资源
# Alt + Home显示导航条F11书签开关
# Ctrl + Shift + F11书签助记开关
# Ctrl + #[0-9]跳转到标识的书签
# Shift + F11显示书签
#
# 6、搜索相关(Usage Search)
# Alt + F7/Ctrl + F7文件中查询用法
# Ctrl + Shift + F7文件中用法高亮显示
# Ctrl + Alt + F7显示用法
#
# 7、重构(Refactoring)
# F5复制F6剪切
# Alt + Delete安全删除
# Shift + F6重命名
# Ctrl + F6更改签名
# Ctrl + Alt + N内联
# Ctrl + Alt + M提取方法
# Ctrl + Alt + V提取属性
# Ctrl + Alt + F提取字段
# Ctrl + Alt + C提取常量
# Ctrl + Alt + P提取参数
#
# 8、控制VCS/Local History
# Ctrl + K提交项目
# Ctrl + T更新项目
# Alt + Shift + C查看最近的变化
# Alt + BackQuote(’)VCS快速弹出
#
# 9、模版(Live Templates)
# Ctrl + Alt + J当前行使用模版
# Ctrl +Ｊ插入模版
#
# 10、基本(General)
# Alt + #[0-9]打开相应的工具窗口
# Ctrl + Alt + Y同步
# Ctrl + Shift + F12最大化编辑开关
# Alt + Shift + F添加到最喜欢
# Alt + Shift + I根据配置检查当前文件
# Ctrl + BackQuote(’)快速切换当前计划
# Ctrl + Alt + S　打开设置页
# Ctrl + Shift + A查找编辑器里所有的动作
# Ctrl + Tab在窗口间进行切换
# 一些常用设置：
#
# 1. pycharm默认是自动保存的，习惯自己按ctrl + s 的可以进行如下设置：
# 1. file -> Setting -> General -> Synchronization -> Save files on frame deactivation 和 Save files automatically if application is idle for .. sec 的勾去掉
# 2. file ->Setting -> Editor -> Editor Tabs -> Mark modified tabs with asterisk 打上勾
# 2. Alt + Enter: 自动添加包
#
# 3. 对于常用的快捷键，可以设置为visual studio(eclipse...)一样的：
# file -> Setting -> Keymap -> Keymaps -> vuisual studio -> Apply
#
# 4. Pycharm中默认是不能用Ctrl+滚轮改变字体大小的，可以在file -> Setting ->Editor-〉Mouse中设置
#
# 5. 要设置Pycharm的字体，要先在file -> Setting ->Editor-〉Editor中选择一种风格并保存，然后才可以改变
#
# 6. 在setting中搜索theme可以改变主题，所有配色统一改变


# PEP8 Python 编码规范整理
# 07/17. 2014
# 决定开始Python之路了，利用业余时间，争取更深入学习Python。编程语言不是艺术，而是工作或者说是工具，所以整理并遵循一套编码规范是十分必要的。所以今天下午我根据PEP 8整理了一份，以后都照此编码了，还会持续更新。
#
# PEP8 Python 编码规范
#
# 一 代码编排
# 1 缩进。4个空格的缩进（编辑器都可以完成此功能），不使用Tap，更不能混合使用Tap和空格。
# 2 每行最大长度79，换行可以使用反斜杠，最好使用圆括号。换行点要在操作符的后边敲回车。
# 3 类和top-level函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。
#
# 二 文档编排
# 1 模块内容的顺序：模块说明和docstring—import—globals&constants—其他定义。其中import部分，又按标准、三方和自己编写顺序依次排放，之间空一行。
# 2 不要在一句import中多个库，比如import os, sys不推荐。
# 3 如果采用from XX import XX引用库，可以省略‘module.’，都是可能出现命名冲突，这时就要采用import XX。
#
# 三 空格的使用
# 总体原则，避免不必要的空格。
# 1 各种右括号前不要加空格。
# 2 逗号、冒号、分号前不要加空格。
# 3 函数的左括号前不要加空格。如Func(1)。
# 4 序列的左括号前不要加空格。如list[2]。
# 5 操作符左右各加一个空格，不要为了对齐增加空格。
# 6 函数默认参数使用的赋值符左右省略空格。
# 7 不要将多句语句写在同一行，尽管使用‘；’允许。
# 8 if/for/while语句中，即使执行语句只有一句，也必须另起一行。
#
# 四 注释
# 总体原则，错误的注释不如没有注释。所以当一段代码发生变化时，第一件事就是要修改注释！
# 注释必须使用英文，最好是完整的句子，首字母大写，句后要有结束符，结束符后跟两个空格，开始下一句。如果是短语，可以省略结束符。
# 1 块注释，在一段代码前增加的注释。在‘#’后加一空格。段落之间以只有‘#’的行间隔。比如：
#
# # Description : Module config.
# #
# # Input : None
# #
# # Output : None
# 2 行注释，在一句代码后加注释。比如：x = x + 1 # Increment x
# 但是这种方式尽量少使用。
# 3 避免无谓的注释。
#
# 五 文档描述
# 1 为所有的共有模块、函数、类、方法写docstrings；非共有的没有必要，但是可以写注释（在def的下一行）。
# 2 如果docstring要换行，参考如下例子,详见PEP 257
#
# """Return a foobang
#
# Optional plotz says to frobnicate the bizbaz first.
#
# """
# 六 命名规范
# 总体原则，新编代码必须按下面命名风格进行，现有库的编码尽量保持风格。
# 1 尽量单独使用小写字母‘l’，大写字母‘O’等容易混淆的字母。
# 2 模块命名尽量短小，使用全部小写的方式，可以使用下划线。
# 3 包命名尽量短小，使用全部小写的方式，不可以使用下划线。
# 4 类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。
# 5 异常命名使用CapWords+Error后缀的方式。
# 6 全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是__all__机制;二是前缀一个下划线。
# 7 函数命名使用全部小写的方式，可以使用下划线。
# 8 常量命名使用全部大写的方式，可以使用下划线。
# 9 类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
# 9 类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
# 11 类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。
# 12 为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。
# 13 类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。
#
# 七 编码建议
# 1 编码中考虑到其他python实现的效率等问题，比如运算符‘+’在CPython（Python）中效率很高，都是Jython中却非常低，所以应该采用.join()的方式。
# 2 尽可能使用‘is’‘is not’取代‘==’，比如if x is not None 要优于if x。
# 3 使用基于类的异常，每个模块或包都有自己的异常类，此异常类继承自Exception。
# 4 异常中不要使用裸露的except，except后跟具体的exceptions。
# 5 异常中try的代码尽可能少。比如：
#
# try:
# value = collection[key]
# except KeyError:
# return key_not_found(key)
# else:
# return handle_value(value)
# 要优于
#
# try:
# # Too broad!
# return handle_value(collection[key])
# except KeyError:
# # Will also catch KeyError raised by handle_value()
# return key_not_found(key)
# 6 使用startswith() and endswith()代替切片进行序列前缀或后缀的检查。比如
#
# Yes: if foo.startswith(‘bar’):优于
# No: if foo[:3] == ‘bar’:
# 7 使用isinstance()比较对象的类型。比如
# Yes: if isinstance(obj, int): 优于
# No: if type(obj) is type(1):
# 8 判断序列空或不空，有如下规则
# Yes: if not seq:
# if seq:
# 优于
# No: if len(seq)
# if not len(seq)
# 9 字符串不要以空格收尾。
# 10 二进制数据判断使用 if boolvalue的方式。
# typo: in word
# 打开 设置，搜索「typo」，看到有个 Spelling - Typo，取消勾选。试试看行不行。我是这样处理的。
# 另外在 IDE Settings - Colors & Fonts - General 里也有 Typo 项，你把效果取消试一下。
# 在设置下搜索weak Waring 去掉勾选的Effects


# Python(7) 编写规范 pep8 的问题笔记
#
# 在学习过程中有如下问题，做个记录。
# 　　以前没有注意的问题
# 1)
# 一行列数 : PEP 8 规定为 79 列，这个太苛刻了，如果要拼接url一般都会超。
# 一个函数 : 不要超过 30 行代码, 即可显示在一个屏幕类，可以不使用垂直游标即可看到整个函数。
# 一个类 : 不要超过 200 行代码，不要有超过 10 个方法。
# 一个模块 : 不要超过 500 行。
#
# 2)不要在一句import中多个库
# 不推荐
# import os, sys
#
# 推荐
# import os
# import sys
#
# 　　在整理自己代码的时候记录的问题。
#
# 错误记录：W292 no newline at end of file
# 处理：打个回车有新的一空行即可（新行不要有空格）。
#
# 错误记录：E302 expected 2 blank lines, found 1
# 处理：上面只有一行空白，但是需要两个空白行
#
# 错误记录：E231 missing whitespace after ‘,’
# 翻译：“，”后要有空格
# 举例：
# 错误 print(“%s %s %s %s %s %s” % (A,B,D,E,K,L))
# 正确 print(“%s %s %s %s %s %s” % (A, B, D, E, K, L))
#
# 错误记录：E225 missing whitespace around operator
# 翻译：
# 举例：
# 错误 print(“%s %s %s %s %s %s”%(A, B, D, E, K, L))
# 正确 print(“%s %s %s %s %s %s”% (A, B, D, E, K, L))
#
# 错误记录：E225 missing whitespace around operator
# 举例：
# 错误 f=open(“D:\\test.txt”, “ab”)
# 正确 f = open(“D:\\test.txt”, “ab”)

