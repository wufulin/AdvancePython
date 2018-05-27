# encoding: utf-8
a = 1
b = 'abc'
print(type(1))
print(type(int))
print(type(b))
print(type(str))

# type->int
#     ->str
# type->class->obj

# object是最顶层的基类
# type也是一个类，同时type也是一个对象
class Student:
	pass

stu = Student()
print(type(stu))
print(type(Student))
print(Student.__bases__)
print(int.__bases__)
print(str.__bases__)
print(type(object))
print(type.__bases__)
print(object.__bases__)
