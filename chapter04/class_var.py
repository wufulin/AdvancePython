# coding:utf-8
__author__ ='wufulin'

class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2,3)
b = A(4,5)
a.aa = 100 # 实例的属性
print(a.x, a.y, a.aa) # 向上查找
print(A.aa)
# print(id(a.aa))
# print(id(b.aa))