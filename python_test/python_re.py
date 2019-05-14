# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re

# 正则表达式相关细节
# re.match() 匹配从头开始的字符串
print re.match("www", "www.rainmtime.com").span()
print re.match("com", "www.rainmtime.com")

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchobj.group():", matchObj.group()
    print "matchobj.group(1):", matchObj.group(1)
    print "matchobj.group(2):", matchObj.group(2)
else:
    print "No match!"

if searchObj:
    print "searchObj.group() : ", searchObj.group()
    print "searchObj.group(1) : ", searchObj.group(1)
    print "searchObj.group(2) : ", searchObj.group(2)
else:
    print "Nothing found!!"

# re.search() 扫描整个字符串，并返回第一个成功的匹配
print re.search("www", "www.rainmtime.com").span()
print re.search("com", "www.rainmtime.com").span()

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

# 检索和替换
phone = "2004-959-559 # 这是一个国外电话号码"

num = re.sub(r'#.*$', "", phone)
print "电话号码是：", num

num = re.sub(r'\D', "", phone)
print "电话号码是:", num

# re.compile 函数，用于把一个字符串，编译成正则表达式
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four', 3, 10)
print m

# findall  是匹配所有，而match 和search 是匹配一次
it = re.findall(r"\d+", "12a32bc43jf3")
print it

# 正则匹配，书写相关逻辑，务必参考对应手册进行书写。
# https://www.runoob.com/python/python-reg-expressions.html

