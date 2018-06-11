# coding:utf-8
__author__ ='wufulin'

def get_url(url):
    # do something 1
    # html = get_html(url) # 此处暂停，切换到另一个函数去执行
    # parse html
    # urls = parse_url(html)
    pass

def get_url2():
    # do something 1
    # html = get_html(url) # 此处暂停，切换到另一个函数去执行
    # parse html
    # urls = parse_url(html)
    pass


# 传统函数调用 过程 A->B->C
# 我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
# 出现了协程 -> 有多个入口的函数， 可以暂停的函数， 可以暂停的函数(可以向暂停的地方传入值)
