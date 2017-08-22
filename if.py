# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:04:38 2017

@author: Administrator
"""

# 例3：if语句多个条件
 
num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello
 
num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine
 
num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine



#为循环做准备
print range(3)  #[0, 1, 2]
print range(10,20)#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]