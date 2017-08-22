#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
#Numbers（数字）
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型

del miles #del语句删除一些 Number 对象引用
#String（字符串）
str = 'Hello World!'# 字符串， 单引号
 
print str           # 输出完整字符串
#字符串格式化
print "My name is %s and weight is %d kg!" % ('Zara', 21)  
print str.upper()# 字符串转成大写  HELLO WORLD!
#List（列表）
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
print list[1:3]          # 输出第二个至第三个的元素
print len(list)

#Tuple（元组）,相当于只读列表
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
print tuple[1:3]          # 输出第二个至第三个的元素 
print len(tuple)
#Dictionary（字典）,讲究顺序
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','dept': 'sales','code':6734 }
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

print len(dict) #2


 

