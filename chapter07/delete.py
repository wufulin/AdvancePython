# coding: utf-8
__author__ = 'wufulin'

# python中的垃圾回收算法是采用 引用计数
a = object()
b = a
del b
print(a)

class A:
    def __del__(self):
        pass