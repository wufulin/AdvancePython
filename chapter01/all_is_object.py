# -*- coding:utf-8 -*-
__author__ = 'wufulin'


# 函数和类也是对象
def ask(name='bobby'):
	print(name)


class Person:
	def __init__(self):
		print('bbb')


def decorator_func():
	print('dec start')
	return ask

my_dec_ask = decorator_func()
my_dec_ask()

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
# 	print(item())

# my_func = ask
# my_func('abc')
#
# my_class = Person
# my_class()
