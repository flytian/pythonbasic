# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:03:50 2017

@author: Administrator
"""

class Employee:
   '所有员工的基类'
   empCount = 0#静态变量
 
   def __init__(self, name, salary):  #构造方法，调用时不必传入self
      self.name = name
      self.salary = salary
      Employee.empCount += 1  #静态变量
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):  #成员方法
      print "Name : ", self.name,  ", Salary: ", self.salary
      
      
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
emp = Employee('flytian',10000)#调用 __init__
emp.displayCount()
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

t = Test()
t.prt()