# coding:utf-8
__author__ ='wufulin'

class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


class User:
    def __init__(self, birthday):
       self.__birthday = birthday   # 私有属性
    
    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year


class Student(User):
    def __init__(self, birthday):
       self.__birthday = birthday   # 私有属性


if __name__ == "__main__":
    user = User(Date(1990, 2, 1))
    # print(user.__birthday)
    # _classname__attribute
    # print(user._User__birthday)
    print(user.get_age())