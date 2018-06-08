# coding:utf-8
__author__ ='wufulin'

# set 集合
# fronzenset 不可变集合 无序， 不重复

# s = set('abced')
# s = set(['a','c','e'])
s = {'a', 'b'}

s1 = frozenset("abcde") # 可以作为dict的key
print(s1)

# set性能很高
# 向set添加数据
s.add('e')
s.add(1)
another_set = set("def")
# s.update(another_set)
re_set = s.difference(another_set)
re_set = s & another_set
# | & - 集合运
print(re_set)

print(s.issubset(re_set))