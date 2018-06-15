# coding:utf-8
__author__ ='wufulin'

# array, deque
# 数组
import array
# array和list的一个重要区别， array只能存放指定的数据类型
my_array = array.array("i")
my_array.append(1)
my_array.append(2)
print(my_array)

def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint
        else:
            return midpoint

a = [9, 18, 19]
print(binary_search(19, a))