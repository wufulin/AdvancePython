# -*- coding:utf-8 -*-
__author__ = 'wufulin'


class Company(object):
	def __init__(self, employee_list):
		self.employee = employee_list

	def __getitem__(self, item):
		return self.employee[item]

company = Company(["tom", "bob", "Coc"])
# employee = company.employee
for em in company:
	print(em)
