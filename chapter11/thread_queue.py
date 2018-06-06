# coding:utf-8
__author__ ='wufulin'

# 线程间通信
import time
import threading
from chapter11 import variables

def get_detail_html():
    # 爬取文章详情页
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            #for url in detail_url_list:
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")


def get_detail_url():
    # 爬取文章列表页
    detail_url_list = variables.detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://www.baidu.com/{id}".format(id=i))
        print("get detail url end")


# 1.线程通信方式-共享变量
if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url)
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()

    start_time = time.time()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time()-start_time))