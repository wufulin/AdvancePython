# coding:utf-8
__author__ ='wufulin'

# 我们去检查某个类是否有某种方法
class Company(object):
	def __init__(self, employee_list):
		self.employee = employee_list

	def __len__(self):
		return len(self.employee)

com = Company(["bobby1","bobby2"])
# print(hasattr(com, "__len__"))

# 1、我们在某些情况之下希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(com, Sized))
# print(len(com))

# 2、我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，集成cache(redis, cache, memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

import abc
# from collections.abc import *
class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass
    
    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    def set(self, key, value):
        pass

# ImoocWeb
# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError


# class RedisCache(CacheBase):
#     pass

# redis_cache = RedisCache()
# redis_cache.set("1", "abc")