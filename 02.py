# 2
'''
2 请实现满足以下三项要求的程序。
(1) 随机生成20个[0, 200]范围内的整数，且每个数大小不同。
(2) 从这20个数中挑选出：奇数，且能够被3整除的数。
(3) 给出（2）中挑选出来的数字的和。
'''
import random
# phase 1
l = []
while(True):
    if len(l) == 20:
        break
    x = random.randint(0, 200)
    if x not in l:  # did not exist in list
        l.append(x)

# phase 2
print('rand list L:', l)
print('numbers in L that can be divided by 3: ', end='')
s = []
for i in l:
    if not i % 3:  # can be divided by 3
        print(i, end=' ')
        s.append(i)
print()
# phase 3
print('sum of those numbers:', sum(s))
