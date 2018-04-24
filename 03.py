# 3
from random import randint
# init list with no duplication in range(0,5)
def getl(l):
    l = []
    while(True):
        if len(l) == 5:
            break
        x = randint(1, 5)
        if x not in l:
            l.append(x)
    return l
    # print(l)


# loop until all condition are satisfied
while(True):
    l = []
    l = getl(l)
    # take l[0] for A and l[1] for B...
    # l[n] represents the ranking of n is l[n]
    a = [(l[1] == 2 and l[0] != 3), (l[1] != 2 and l[0] == 3)]
    b = [(l[1] == 2 and l[4] != 4), (l[1] != 2 and l[4] == 4)]
    c = [(l[2] == 1 and l[3] != 2), (l[2] != 1 and l[3] == 2)]
    d = [(l[2] == 5 and l[3] != 3), (l[2] != 5 and l[3] == 3)]
    e = [(l[4] == 4 and l[0] != 1), (l[4] != 4 and l[0] == 1)]
    if True in a and True in b and True in c and True in d and True in e:  # judge
        print(a, b, c, d, e)
        print(l)
        break

# print(a,b,c,d,e)
    # if


"""
歌手排名预测
Ａ歌手说：Ｂ第二，我第三；
Ｂ歌手说：我第二，Ｅ第四；
Ｃ歌手说：我第一，Ｄ第二；
Ｄ歌手说：Ｃ最后，我第三；
Ｅ歌手说：我第四，Ａ第一；
歌王之战结果出来后，每位歌手的预测都只说对了一半，即一对一错。请编程给出比赛的实际名次（将ABCDE按名次顺序排序，例如BCEAD代表B是第一名，D是最后一名）。

output:
[False, True] [False, True] [False, True] [True, False] [True, False]
[3, 1, 5, 2, 4]
"""
