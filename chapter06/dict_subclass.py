# coding:utf-8
__author__ ='wufulin'

# 不建议继承dict和list
# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)

# my_dict = Mydict(one=1)
# my_dict["two"] = 2
# print(my_dict)

from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value**2)


my_dict = Mydict(one=3)
# my_dict["two"] = 2
print(my_dict)

from collections import defaultdict

my_dict = defaultdict(int)
my_value = my_dict['bobby']
print(my_value)
