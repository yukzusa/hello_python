#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print (counter)
print (miles)
print ( name)

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list)  # 输出完整列表
print (list[0])  # 输出列表的第一个元素
print (list[1:3])  # 输出第二个至第三个元素
print (list[2:] ) # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)  # 输出列表两次
print (list + tinylist)   # 打印组合的列表



tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

a = 21
b = 10
c = 0
c = a + b
print("1 - c 的值为：", c)
c = a - b
print ("2 - c 的值为：", c)
c = a * b
print ("3 - c 的值为：", c)
c = a / b
print ("4 - c 的值为：", c)
c = a % b
print ("5 - c 的值为：", c)
# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)
a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)

a = 21
b = 10
c = 0
if a == b:
    print
    ("1 - a 等于 b")
else:
    print
    "1 - a 不等于 b"
if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a != b:
    print ("3 - a 不等于 b")
else:
    print
    "3 - a 等于 b"

if a < b:
    print
    "4 - a 小于 b"
else:
    print
    "4 - a 大于等于 b"

if a > b:
    print
    "5 - a 大于 b"
else:
    print
    "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print
    "6 - a 小于等于 b"
else:
    print
    "6 - a 大于  b"

if b >= a:
    print
    "7 - b 大于等于 a"
else:
    print
    "7 - b 小于 a"