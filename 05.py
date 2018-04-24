"""任意一个４位自然数，将组成该数的各位数字重新排列，形成一个最大数和一个最小数，之后两数相减，其差仍为一个自然数。重复进行上述运算，你会发现一个神秘的数。
要求：
（1）编程来找到这个神秘的数。
（2）随机生成5个4位自然数，打印中间结果并验证结论。

"""
# 5
import random
n = random.randint(1000, 9999)
# get random natural number with four digit
print('natural num generated: ', n)
cur = 0  # remember current result


def black_hole(n):
    global cur
    l = list(str(n))
    l.sort(reverse=True)  # sort the list desc
    xm = xn = 0
    for i in range(4):
        xm *= 10
        xm += int(l[i])
        xn *= 10
        xn += int(l[4-i-1])
        # xm is the largest num and xn is the smallest
    if xm-xn != cur:
        print('current result:', xm-xn)
        cur = xm-xn
        black_hole(xm-xn)
        # calculate until the result did not change
    else:
        print("Get! result=", xm-xn)


if __name__ == '__main__':
    black_hole(n)

"""
output(sample):
natural num generated:  9721
current result: 8442
current result: 5994
current result: 5355
current result: 1998
current result: 8082
current result: 8532
current result: 6174
Get! result= 6174
"""
