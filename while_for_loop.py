# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:11:43 2017

@author: Administrator
"""

numbers = [12, 37, 5, 43, 8, 3]
even = [] #偶数
odd = []  #奇数
while len(numbers) > 0:
    number = numbers.pop()#从列表后面开始弹出
    if number %2 == 0:
        even.append(number)
    else:
        odd.append(number)

print even 
print odd


for letter in 'Python':     # 第一个实例，遍历字符串中的字符
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例，遍历列表中的字符串
   print '当前水果 :', fruit
 
print "Good bye!"


#循环嵌套
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1
 
print "Good bye!"