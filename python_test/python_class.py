# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "一共 %d" % Employee.empCount

    def displayEmployee(self):
        print "Name:", self.name, ",Salary", self.salary

    def prt(self):
        print self
        print self.__class__

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"


# 创建类的实力
employee = Employee("chunyu", "35000")
employee.prt()
employee.displayEmployee()

# python 内置类属性

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

"""
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""


# 类的继承 class 子类（父类）

class Parent:
    parentAttr = 100

    __privateattr = 0  # 私有变量

    def __init__(self):
        print "父亲类创建了"

    def parentMethod(self):
        print "调用了父亲类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父亲类属性：", Parent.parentAttr

    # 私有方法
    def __privateMethod(self):
        print "哈哈,我是私有方法"


class Child(Parent):
    def __init__(self):
        print "子类创建了"

    def childMethod(self):
        print "调用了子类方法"

    def parentMethod(self):
        print "子类重写了 parentMethod 方法"


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr("haha")
c.getAttr()


# 运算符重载演示(重载了+号)：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

# 关于单下划线、双下划线、头尾双下划线说明
"""
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
"""
