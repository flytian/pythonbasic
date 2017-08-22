# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:10:55 2017

@author: Administrator
"""

class Parent:        # 定义父类
   parentAttr = 100#静态变量
   def __init__(self):
      print "调用父类构造函数"
 
   def parentMethod(self):
      print '调用父类方法'
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print "父类属性 :", Parent.parentAttr
 
class Child(Parent): # 定义子类
   def __init__(self):#在继承中基类的构造（__init__()方法）不会被自动调用
      print "调用子类构造方法"
 
   def childMethod(self):
      print '调用子类方法 child method'
 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法