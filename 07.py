# 7
'''
设计函数实现微信发红包的功能。
要求：
（1）输入：拟发红包的总额，拟派发的人数。
（2）输出：列表形式的派发方案。派发方案是随机的，要求给出10次模拟的结果。
（3）总额与每人得到的金额皆为整数。
（4）任何人不能得到0元的红包。
例：总额20元，派发人数：5
某次随机模拟的结果为：[3, 7, 8, 1, 1]
'''
# 7
import random


def pocket_Money():
    """
    distribute pocket money!
    """
    while(True):
        try:
            num = int(input("person num(派发人数):"))
            money = int(input("tatal money(总额):"))
        except ValueError:
            print("Please input the int!")
        else:
            if money >= num:
                break
            else:
                print("number of money should be larger than people. Input again")

    # get the input
    l = []
    for i in range(num):
        l.append(1)
    for i in range(money-num):
        pos = random.randint(0, num-1)
        l[pos] += 1
    # simulate the distribution
    print('simulation result:', l)
    print('sum of list above:', sum(l), 'length of list above:', len(l))


if __name__ == '__main__':
    pocket_Money()
    """
    result sample:
    person num(派发人数):10
    tatal money(总额):50
    [6, 1, 4, 8, 5, 6, 6, 4, 4, 6]
    """
