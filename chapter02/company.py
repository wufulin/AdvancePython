# -*- coding:utf-8 -*-
__author__ = 'wufulin'


class Company(object):
	def __init__(self, employee_list):
		self.employee = employee_list

	def __str__(self):
		return ",".join(self.employee)

	def __repr__(self):
		return ",".join(self.employee)

	def __getitem__(self, item):
		return self.employee[item]

	def __len__(self):
		return len(self.employee)


class MyVector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return MyVector(self.x + other.x, self.y + other.y)

	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)

first_vector = MyVector(1, 1)
second_vector = MyVector(2, 2)
print(first_vector + second_vector)

company = Company(["tom", "bob", "Coc"])
# employee = company.employee
print(company)
for em in company:
	print(em)
