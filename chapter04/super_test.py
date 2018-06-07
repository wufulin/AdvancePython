# coding:utf-8
__author__ ='wufulin'

class A:
    def __init__(self):
        print ("A")


class B(A):
    def __init__(self):
        print ("B")
        super().__init__()


from threading import Thread
class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)

# 既然我们重写B的构造函数，为什么还要去调用super
# super到底执行顺序是什么样的 --> MRO

class C(A):
    def __init__(self):
        print ("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

if __name__ == "__main__":
    print(D.__mro__)
    d = D()
    # b = B()
    # print()