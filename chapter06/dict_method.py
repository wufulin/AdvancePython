# coding:utf-8
__author__ ='wufulin'

a = {
    "bobby1": {
        "company": 'abc'
    },
    "bobby2": "bb"
}

# clear
# a.clear()

# copy 返回浅拷贝
# new_dict = a.copy()
# new_dict["bobby1"]["company"] = "imooc3"
# print(new_dict)

# 深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"] = "imooc3"
print(new_dict)
print(a)

# fromkeys
new_list = ['bobby1','bobby2','bobby3']
new_dict = dict.fromkeys(new_list, {"a":1})
print(new_dict)

# get
print(new_dict.get("bobby4", {}))

# items
for key, value in new_dict.items():
    print(key, value)

# setdefault
default_value = new_dict.setdefault("bobby", 2)
print(default_value)

# update
new_dict.update({"bobby": "imooc"})
print(new_dict)