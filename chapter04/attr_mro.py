# coding:utf-8
__author__ ='wufulin'

# 类属性和实例属性的查找顺序
class A:
    name = 'A'
    def __init__(self):
        self.name = 'obj'

# C3算法
a = A()
print(a.name)

# 新式类
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class M(B, C):
    pass

print(M.__mro__)