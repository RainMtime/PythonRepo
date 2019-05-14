# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
# 读取键盘操作
def raw_input_test():
    str = raw_input("请输入：")
    print "你输入的内容是：", str


# input读取键盘操作，但是其可以接受一个python表达式作为输入，并将运算结果返回。
def input_test():
    str = input("请输入：")
    print "你输入的内容是：", str


def open_file(filename="/Users/chunyu/Desktop/code/pythonDemo/file.txt"):
    fo = open(filename, "w")
    print "文件名：", fo.name
    print "是否已关闭:", fo.closed
    print "访问模式:", fo.mode
    fo.write("hello RainMtime！！,有空喝\n喜茶哈")
    fo.close()
    # fo.tell()告诉当前的读写位置是哪里
    # fo.seek()可以跳跃一些文件位置。
    fo_read = open(filename, "r+")
    # import os
    # os.rename()重新命名
    # os.remove()方法删除文件
    # os.mkdir()方法，是创建一个文件夹
    # os.rmdir()方法，删除目录，在删除目录之前需要注意应该提前清楚其子文件。
    # os.chdir("/home") #进入文件夹/home目录
    # print os.getcwd()


    str = fo_read.read(10)
    print str
    fo_read.close()


if __name__ == "__main__":
    # 测试案例[x*5 for x in range(2,10,2)]
    # input_test()

    open_file()


