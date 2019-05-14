# !/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import threading
import time


# 为线程定一个函数

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s:%s" % (threadName, time.ctime(time.time()))


# 多线程测试模块（thread 模块方式，较为原始）
"""
try:
    thread.start_new_thread(print_time, ("Thread-1", 2))
    thread.start_new_thread(print_time, ("Thread-2", 5))
except:
    print "Error:unable to start thread"
while 1:
    pass
"""


def print_info(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


# 使用Threading 模块创建线程
exitFlag = 0

threadLock = threading.Lock()


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        threadLock.acquire()
        print "Starting :" + self.name
        print_info(self.name, 2, self.counter)
        print "Exiting" + self.name
        threadLock.release()


thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 5)

thread1.start()
thread2.start()
#  主线程等待自线程执行完毕，才会往下走。Join()的用法
thread1.join()
thread2.join()
print "Exiting Main Thread"

# 线程优先队列 Queue
