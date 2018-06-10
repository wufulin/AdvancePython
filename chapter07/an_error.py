# coding: utf-8
__author__ = 'wufulin'

def add(a, b):
    a += b
    return a

class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == '__main__':
    # a = 1
    # b = 2
    a = [1,2]
    b = [3,4]
    c = add(a, b)
    print(c)
    print(a, b)

    com2 = Company('com2')
    com2.add('bobby')
    print(com2.staffs)
    print(Company.__init__.__defaults__)

    com3 = Company('com3')
    com3.add('bobby3')
    print(com2.staffs)
    print(com3.staffs)