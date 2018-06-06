# coding:utf-8
__author__ ='wufulin'

class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def tomorrow(self):
        self.day += 1

    # 静态方法
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0 and (int(month) > 0 and int(month) <=12) and (int(day)>0 and int(day)<=31):
            return True
        else:
            return False 

    # 类方法
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()
    print(new_day)

    # 2018-12-31
    date_str = '2018-12-21'
    # year, month, day = tuple(date_str.split('-'))
    
    # 用static method完成初始化
    new_day1 = Date.parse_from_string(date_str)
    print(new_day1)
    
    # 用class method完成初始化
    new_day2 = Date.from_string(date_str)
    print(new_day2)
    print(Date.valid_str("2018-13-12"))