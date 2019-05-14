# !/usr/bin/python
# -*- coding: UTF-8 -*-
import time
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
    print str * 2
    # 字符串格式化
    print "my name is %s and age is %d" % ("chunyu", 25)

    # List 列表
    print "List 列表"
    list = ['runoob', 786, 2.23, 'john', 70.2]
    tinylist = [123, 'john']
    print list
    print list[0]
    print list[1:3]
    print list[2:]
    print tinylist * 2
    print  list + tinylist
    del list [0]
    print list

    # tuple 元组
    print "tuple 元组"
    tuplesample = ('runbo', 786, 2.23, 'john', 70.2)
    tinytuple = (1234, 'hon')

    print tuplesample
    print tuplesample[0]
    print tuplesample[:3]
    print tinytuple * 2
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

    # python 运算符
    print "python 运算符"
    a = 10
    b = 2
    c = 0

    c = a + b
    print "a+b的值:", c
    c = a - b
    print "a -b 的值：", c
    # a的b 次方
    c = a ** b
    # a//b 取商的余数

    # python 的比较符号（== != <> >= <= < >）
    a = 21
    b = 10
    c = 0

    if a == b:
        print "1-a 等于b"
    else:
        print "1-a 不等于 b"

    if a != b:
        print "2-a 不等于 b"
    else:
        print "2-a 等于b"
    # 比较2个运算符是否不等于
    if a <> b:
        print "3-a 不等于b"
    else:
        print "3-a 等于b"

    # python 赋值运算符(=,+=,-=,**=,//=,/=,*=)


    # python  位运算符(&,|,^,~,<<,>>2)

    # ptyhon 逻辑运算符(and,or, not)

    # python 成员运算符

    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    if (a in list):
        print "1- 变量a 在给定的列表list中"
    else:
        print "1 - 变量a 未再给定的列表list中"

    if (a not in list):
        print "2- 变量a 不在连标list中"
    else:
        print "2- 变量a 在列表list中"

    # python 身份验证符（is， not is ）

    # is 是判断两个标示符是不是饮用同一个对象
    # not is 是相反的意思

    a = 20
    b = 20

    if (a is b):
        print "a和b 是相同引用"
    else:
        print "a 和b 是不相同的引用"

    # python 条件语句
    if a == b:
        print "a ==b"
    elif a > 10:
        print "a>10"
    else:
        print "a!=b"

    # python  循环语句
    print "python  循环语句-for"

    n = 0
    for i in range(5):

        if i == 1:
            n += 2
            break
        else:
            n += 1
            continue
    print n

    for letter in "python":
        print "当前字母:", letter

    fruits = ['banana', 'apple', 'mango']

    for fruit in fruits:
        print "当前的水果:", fruit

    print "python  循环语句-while"
    while n > 0:
        n -= 1
        print n

    # python 的pass 语句(pass 是空语句，是为了保持程序结构的完整性，不做任何事情）
    for letter in 'python':
        if letter == 'h':
            pass
            print '这个是pass快'
        print '当前字母：', letter

    # python 三引号（triple quotes,允许一个字符串跨多行，字符串可以包含换行符和制表符)
    print ''' hi,
    pretty girl!
    '''
    print '''hi,\n pretty girl ,have you boy friend?'''

    # python Unicode 字符串

    unicodestr = u'Hello\u0020World!'
    print  unicodestr

    #python 时间和日期
    ticks = time.time()
    print "当前的时间:",ticks

    localtime = time.localtime(time.time())
    print "本地时间为:",localtime

    #格式化时间：
    print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    #将格式字符串转换成时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

    #try catch 捕获
    try:
        raise IOError,"ioerror"
        fh = open("testfile","w")
        fh.write("这是一个测试文件,用于测试异常!!")
    except IOError:
        print "Error:没有找到相应"
    else:
        print "内容写入成功"
    finally:
        print "哈哈我是finally，必须执行"






"""
python 中的多行
注释使用 3个双引号
～.～!!
"""
