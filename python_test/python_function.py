# !/usr/bin/python
# -*- coding: UTF-8 -*-


def functionName(parameters):
    "？？？这tm啥玩意？"
    print parameters
    return


def printinfo(name, age=18):
    print "年龄是:", age
    print "名字是:", name
    return


def printSchool(name, age, *vartuple):
    print vartuple[0]
    print vartuple[1]


#命名空间和作用域
Money =2000

def AddMoney():
    global Money
    Money = Money + 1



# 匿名函数(利用lamda）
sum = lambda arg1, arg2: arg1 + arg2

if __name__ == '__main__':
    # 关键字参数，可以忽略参数顺序
    functionName(parameters="hello world!")
    # 演示了一下，默认参数的使用
    printinfo(name="chunyu")
    printSchool("chunyu", 18, "name", "hello ?")
    print  sum(10, 20)

    print Money
    AddMoney()
    print Money

    globalss = globals()
    # globals()和 locals()可以查看当前作用域内部，能够访问到的相关函数。
    print locals()

    #reload 重载相关模块，因为载入模块的时候，模块顶层代码逻辑会被执行一边。



