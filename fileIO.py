# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:53:47 2017

@author: Administrator
"""

fo = open("foo.txt", "ab+")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
#写入数据
fo.write( "www.runoob.com!\nVery good site!\n");
#读取10个字符
str = fo.read(10);
print "读取的字符串是 : ", str

# 查找当前位置
position = fo.tell();
print "当前文件位置 : ", position
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print "重新读取字符串 : ", str

# 关闭打开的文件
fo.close()