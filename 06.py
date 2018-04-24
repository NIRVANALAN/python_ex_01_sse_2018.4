"""已知一个椭圆的长轴长为10，短轴长为8，请设计算法求这个椭圆的面积，并编程实现。
要求1：利用特卡罗算法进行模拟。
要求2：分别打印在不同点数（至少设置4个不同的点数）情况下面积的近似值。

"""
# 6
# phase 1
import random
import time
iter_num = 10000

def Monte_Calo_oval(iter_n):
    a = 5
    b = 4
    count = 0
    for i in range(iter_n):
        x_rand = random.random()*a
        y_rand = random.random()*b
        if (pow(x_rand, 2)/pow(a, 2)+pow(y_rand, 2)/pow(b, 2) < 1):  # simulate
            count += 1  # document when satisfied
    print('oval area simulated by Monte Carlo when n=',
          iter_n, count/iter_n*4*a*b)

if __name__ == '__main__':
    print('oval properties: a=5 b=4')
    T1 = time.time()  # get cur time
    # area under four different cases
    Monte_Calo_oval(10000)
    Monte_Calo_oval(20000)
    Monte_Calo_oval(25000)
    Monte_Calo_oval(30000)
    print('time consumed:', time.time()-T1)  # total running time
#
