# coding:utf-8
__author__ ='wufulin'

# 容器序列 list tuple deque
my_list = []
my_list.append(1)
my_list.append("a")

# 扁平序列 str bytes bytearray array.array

# 可变序列 list deque bytearray array
# 不可变 str tuple bytes
from collections import abc

a = [1,2]
c = a + [3,4]

# += 就地加  <==> extend
# a += (3,4)
# a.extend(range(3))
a.append((1,2))
print(a)