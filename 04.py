"""效率比较
Python中list类有insert()和append()两个成员函数。
(1) 说明这两个成员函数的作用，联系与区别。
(2) 试编写代码，分别利用这两个函数建立一个长度为50000的列表，列表元素为
为50000~1。
(3) 比较（2）中两者的运行效率，并用程序证明（提示：利用运行时间证明）

"""
import time

# 4
"""
append()方法是指在列表末尾增加一个数据项
insert()方法是指在某一个特定位置增加一个数据项
当insert()中的特定位置为尾部，insert()和append()效果相同。但append()无法在除尾部之外的位置添加元素,insert()每次运行都需要指定插入的位置
append()运行速度更快，代码演示如下
"""

l = []
#-------append--------#
t1 = time.time()  # get current time
for i in range(50000):
    l.append(i)
print('append time: ', time.time()-t1)
l.clear()  # clear the list
t1 = time.time()
#-------insert--------#
for i in range(50000):
    l.insert(i, i)
print('insert time:  ', time.time()-t1)
"""
output(sample):
append time:  0.0060160160064697266
insert time:   0.010026216506958008
"""
