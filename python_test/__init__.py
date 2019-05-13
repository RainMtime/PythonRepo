# !/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    # print 换行与否演示
    print "换行hello"
    print "RainMtime"
    print "不换行 Hello",
    print "RainMtime"

    # 变量创建和赋值(必须赋值，并且在内存中存在)
    counter = 100
    mile = 1000.0
    name = "John"
    a = b = c = 10

    # 标准数据类型只有5种
    # Number （数字，四种类型int ，long ，float，complex(复数））
    # String （字符串）
    # List （列表）
    # Tuple （元组）
    # Dictionary (字典）

    # String类型随意切割，并且应可以从-1开始索引，如下-1 对应字母e
    str = "hello RainMtime"
    # String 类型可以截取一段字符串，以最小波长
    print  str[1:10:2]
    print str*2

    # List 列表
    print "List 列表"
    list = ['runoob' ,786,2.23,'john',70.2]
    tinylist = [123,'john']
    print list
    print list[0]
    print list[1:3]
    print list[2:]
    print tinylist * 2
    print  list + tinylist

    # tuple 元组
    print "tuple 元组"
    tuplesample = ('runbo',786,2.23,'john',70.2)
    tinytuple = (1234,'hon')

    print tuplesample
    print tuplesample[0]
    print tuplesample[:3]
    print tinytuple*2
    print tuplesample + tinytuple

    # dictionary 字典
    print "dictionary 字典"
    dict = {}
    dict['one'] = "this is one"
    dict[2] = "this is two"
    dict[3] = 3

    print dict
    print dict[3]
    print dict.keys()
    print dict.values()











    # for 语句
    n = 0
    for i in range(5):

        if i == 1:
            n += 2
            break
        else:
            n += 1
            continue

    print n

"""
python 中的多行
注释使用 3个双引号
～.～!!
"""
