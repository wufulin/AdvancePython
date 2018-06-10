# coding: utf-8
__author__ = 'wufulin'

# python和java的变量本质不一样，python的变量实质上是一个指针

a = 1
a = [1,2,3]
b = a
print(a is b)
b.append(4)
print(a)