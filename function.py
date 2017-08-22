# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:46:08 2017

@author: Administrator
"""

# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print "函数内 : ", total
   return total;
 
# 调用sum函数
total = sum( 10, 20 );
print "total is: " , total