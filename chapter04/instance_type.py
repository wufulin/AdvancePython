# coding:utf-8
__author__ ='wufulin'

class A:
    pass


class B(A):
    pass

b = B()
print(isinstance(b, B))
print(isinstance(b, A))

# print(id(B))
# print(id(b))
print(type(b) is A)