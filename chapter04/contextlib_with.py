# coding:utf-8
__author__ ='wufulin'

import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print('file open')
    yield {}
    print('file end')


with file_open("bobby.txt") as f_open:
    print("file processing")